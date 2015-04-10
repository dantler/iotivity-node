#include <node.h>
#include <v8.h>

extern "C" {

#include <occoaphelper.h>

}

using namespace v8;

void bind_hello( const FunctionCallbackInfo<Value>& args ) {
	Isolate* isolate = Isolate::GetCurrent();
	HandleScope scope( isolate );

	args.GetReturnValue().Set( String::NewFromUtf8( isolate, "world" ) );
}

void bind_CoAPToOCResponseCode( const FunctionCallbackInfo<Value>& args ) {
	Isolate* isolate = Isolate::GetCurrent();
	HandleScope scope( isolate );

	if ( args.Length() < 1 ) {
		isolate->ThrowException( Exception::TypeError(
			String::NewFromUtf8( isolate, "Need coapCode" ) ) );
		return;
	}

	if ( !args[ 0 ]->IsNumber() ) {
		isolate->ThrowException( Exception::TypeError(
			String::NewFromUtf8( isolate, "coapCode must be a number" ) ) );
		return;
	}

	args.GetReturnValue().Set(
		Number::New( isolate,
			( double )CoAPToOCResponseCode( ( uint8_t )args[ 0 ]->NumberValue() ) ) );
}

void InitFunctions( Handle<Object> exports ) {
	NODE_SET_METHOD( exports, "hello", bind_hello );
	NODE_SET_METHOD( exports, "CoAPToOCResponseCode", bind_CoAPToOCResponseCode );
}
