#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
Name     : qt6languageserver
Version  : 6.6.1
Release  : 6
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtlanguageserver-everywhere-src-6.6.1.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtlanguageserver-everywhere-src-6.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6languageserver-lib = %{version}-%{release}
Requires: qt6languageserver-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6languageserver package.
Group: Development
Requires: qt6languageserver-lib = %{version}-%{release}
Provides: qt6languageserver-devel = %{version}-%{release}
Requires: qt6languageserver = %{version}-%{release}

%description dev
dev components for the qt6languageserver package.


%package lib
Summary: lib components for the qt6languageserver package.
Group: Libraries
Requires: qt6languageserver-license = %{version}-%{release}

%description lib
lib components for the qt6languageserver package.


%package license
Summary: license components for the qt6languageserver package.
Group: Default

%description license
license components for the qt6languageserver package.


%prep
%setup -q -n qtlanguageserver-everywhere-src-6.6.1
cd %{_builddir}/qtlanguageserver-everywhere-src-6.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703006966
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703006966
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6languageserver
cp %{_builddir}/qtlanguageserver-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6languageserver/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtlanguageserver-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6languageserver/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtlanguageserver-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6languageserver/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtlanguageserver-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6languageserver/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtlanguageserver-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6languageserver/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6jsonrpcprivate_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6languageserverprivate_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_jsonrpc_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_languageserver_private.pri
/usr/lib64/qt6/modules/JsonRpcPrivate.json
/usr/lib64/qt6/modules/LanguageServerPrivate.json

%files dev
%defattr(-,root,root,-)
/usr/include/QtJsonRpc/6.6.1/QtJsonRpc/private/qhttpmessagestreamparser_p.h
/usr/include/QtJsonRpc/6.6.1/QtJsonRpc/private/qjsonrpcprotocol_p.h
/usr/include/QtJsonRpc/6.6.1/QtJsonRpc/private/qjsonrpcprotocol_p_p.h
/usr/include/QtJsonRpc/6.6.1/QtJsonRpc/private/qjsonrpctransport_p.h
/usr/include/QtJsonRpc/6.6.1/QtJsonRpc/private/qjsontypedrpc_p.h
/usr/include/QtJsonRpc/6.6.1/QtJsonRpc/private/qtypedjson_p.h
/usr/include/QtJsonRpc/QtJsonRpc
/usr/include/QtJsonRpc/QtJsonRpcDepends
/usr/include/QtJsonRpc/QtJsonRpcVersion
/usr/include/QtJsonRpc/qtjsonrpcglobal.h
/usr/include/QtJsonRpc/qtjsonrpcversion.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageserverbase_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageserverbase_p_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageservergen_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageservergen_p_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageserverjsonrpctransport_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageserverprespectypes_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageserverprotocol_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageserverspec_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlanguageserverspectypes_p.h
/usr/include/QtLanguageServer/6.6.1/QtLanguageServer/private/qlspnotifysignals_p.h
/usr/include/QtLanguageServer/QtLanguageServer
/usr/include/QtLanguageServer/QtLanguageServerDepends
/usr/include/QtLanguageServer/QtLanguageServerVersion
/usr/include/QtLanguageServer/qtlanguageserverglobal.h
/usr/include/QtLanguageServer/qtlanguageserverversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtLanguageServerTestsConfig.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateConfig.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateDependencies.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateTargets.cmake
/usr/lib64/cmake/Qt6JsonRpcPrivate/Qt6JsonRpcPrivateVersionlessTargets.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateConfig.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateDependencies.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateTargets.cmake
/usr/lib64/cmake/Qt6LanguageServerPrivate/Qt6LanguageServerPrivateVersionlessTargets.cmake
/usr/lib64/libQt6JsonRpc.prl
/usr/lib64/libQt6JsonRpc.so
/usr/lib64/libQt6LanguageServer.prl
/usr/lib64/libQt6LanguageServer.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6JsonRpc.so.6
/usr/lib64/libQt6JsonRpc.so.6.6.1
/usr/lib64/libQt6LanguageServer.so.6
/usr/lib64/libQt6LanguageServer.so.6.6.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6languageserver/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6languageserver/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6languageserver/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6languageserver/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6languageserver/f45ee1c765646813b442ca58de72e20a64a7ddba
