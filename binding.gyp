{
	"variables": {
		"IOTIVITY_PATH": '<!(echo "$IOTIVITY_PATH")',
		"LIBCOAP": '<!(find "$IOTIVITY_PATH/out" -name libcoap.a -print -quit)',
		"LIBOCTBSTACK_PATH": '<!(dirname $( find "$IOTIVITY_PATH/out" -name liboctbstack.so -print -quit ))'
	},
	"targets": [
		{
			"target_name": "iotivity",
			"sources": [
				"src/main.cc",
				"src/enums.cc",
				"src/functions/oc-create-delete-resource.cc",
				"src/functions/oc-do-resource.cc",
				"src/functions/simple.cc",
				"src/functions.cc",
				"src/callback-info.c"
			],
			"libraries": [
				"<(PRODUCT_DIR)/libffi.a",
				'<(LIBCOAP)',
				'<(LIBOCTBSTACK_PATH)/liboctbstack.so',
				'-Wl,-rpath,<(LIBOCTBSTACK_PATH)'
			],
			"include_dirs": [
				"<( IOTIVITY_PATH )/resource/csdk/stack/include",
				"<( IOTIVITY_PATH )/resource/csdk/ocsocket/include"
			],
			"conditions": [
				[ "'<!(echo $TESTING)'=='true'",
						{ "defines": [ "TESTING" ] } ]
			],
			"dependencies": [
				"node_modules/ffi/deps/libffi/libffi.gyp:ffi"
			]
		},
		{
			"target_name": "client",
			"type": "executable",
			"sources": [ "c/client.c" ],
			"libraries": [
				'<(LIBOCTBSTACK_PATH)/liboctbstack.so',
				'<(LIBCOAP)',
				'-Wl,-rpath,<(LIBOCTBSTACK_PATH)',
				'<!(pkg-config --libs glib-2.0)',
			],
			"include_dirs": [
				"<( IOTIVITY_PATH )/resource/csdk/stack/include",
				"<( IOTIVITY_PATH )/resource/csdk/ocsocket/include"
			],
			"cflags": [
				'<!(pkg-config --cflags glib-2.0)'
			]
		}
	]
}
