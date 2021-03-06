{
  'includes': [
    'build/config.gypi',
    'nodejs.gypi',
  ],
  'targets': [
    {
      'target_name': 'webrtc-native',
      'type': 'loadable_module',
      'product_extension': 'node',
      'include_dirs': [
        '<(nodedir)/src',
        '<(nodedir)/deps/uv/include',
        '<(nodedir)/deps/v8/include',
        'third_party/webrtc/src/',
        'third_party/webrtc/src/webrtc',
        'third_party/webrtc/src/webrtc/system_wrappers/interface',
        'third_party/webrtc/src/third_party/jsoncpp/source/include',
      ],
      'defines': [
        'BUILDING_NODE_EXTENSION',
        'EXPAT_RELATIVE_PATH',
        'FEATURE_ENABLE_VOICEMAIL',
        'GTEST_RELATIVE_PATH',
        'JSONCPP_RELATIVE_PATH',
        'LOGGING=1',
        'SRTP_RELATIVE_PATH',
        'FEATURE_ENABLE_SSL',
        'FEATURE_ENABLE_VOICEMAIL',
        'FEATURE_ENABLE_PSTN',
        'HAVE_SCTP',
        'HAVE_SRTP',
        'HAVE_WEBRTC_VIDEO',
        'HAVE_WEBRTC_VOICE',
        'LIBPEERCONNECTION_LIB=1'
      ],
      'sources': [
        'src/BackTrace.cc',
        'src/ArrayBuffer.cc',
        'src/EventEmitter.cc',
        'src/Module.cc',
        'src/PeerConnection.cc',
        'src/DataChannel.cc',
        'src/Observers.cc',
        'src/Wrap.cc'
      ],
      'dependencies': [
        '<(DEPTH)/third_party/jsoncpp/jsoncpp.gyp:jsoncpp',
        '<(DEPTH)/talk/libjingle.gyp:libjingle_peerconnection',
      ],
      'conditions': [ 
        ['OS=="linux"', {
          'defines': [
            'LINUX',
            'WEBRTC_LINUX',
            '_LARGEFILE_SOURCE', 
            '_FILE_OFFSET_BITS=64',
          ],
          'cflags': [
            '-std=gnu++11',
            '-fPIC',
            '-Wno-deprecated-declarations',
            '-Wno-newline-eof',
          ],
          'conditions': [
            ['clang==1', {
              'cflags': [
                '-Wall',
                '-Wextra',
                '-Wimplicit-fallthrough',
                '-Wmissing-braces',
                '-Wreorder',
                '-Wunused-variable',
                '-Wno-address-of-array-temporary',
                '-Wthread-safety',
              ],
              'cflags_cc': [
                '-Wunused-private-field',
              ],
            }],
          ],
        }],
        ['OS=="win"', {
          'defines': [
            'WEBRTC_WIN',
          ],
          'msvs_disabled_warnings': [ 
            4251,
            4530,
            4702,
            4199,
          ],
          'libraries': [
            '-lkernel32.lib',
            '-luser32.lib',
            '-lgdi32.lib',
            '-lwinspool.lib',
            '-lcomdlg32.lib',
            '-ladvapi32.lib',
            '-lshell32.lib',
            '-lole32.lib',
            '-loleaut32.lib',
            '-luuid.lib',
            '-lodbc32.lib',
            '-l"<(nodedir)\\<(target_arch)\\node"',
          ],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-std=gnu++0x',
              '-Wno-c++0x-extensions',
              '-Wno-c++11-extensions',
              '-Wno-deprecated-declarations',
              '-Wno-newline-eof',
            ],
            'DYLIB_INSTALL_NAME_BASE': '@rpath',
          },
          'libraries': [ 
            '-undefined dynamic_lookup',
            '-framework AppKit',
            '-framework QTKit',
          ],
          'defines': [
            'USE_BACKTRACE',
            'OSX',
            'WEBRTC_MAC',
            '_LARGEFILE_SOURCE', 
            '_FILE_OFFSET_BITS=64',
            '_DARWIN_USE_64_BIT_INODE=1',
          ],
        }],
        ['OS=="ios"', {
          'defines': [
            'IOS',
            'WEBRTC_MAC',
            'WEBRTC_IOS',
          ],
        }],
        ['os_posix==1', {
          'defines': [
            'HASH_NAMESPACE=__gnu_cxx',
            'WEBRTC_POSIX',
            'DISABLE_DYNAMIC_CAST',
            '_REENTRANT',
          ],
        }],
      ],
    },
    {
      'target_name': 'All',
      'type': 'none',
      'dependencies': [
        'webrtc-native'
      ],
    },
  ],
}