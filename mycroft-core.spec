#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mycroft-core
Version  : v18.8.4
Release  : 5
URL      : https://github.com/MycroftAI/mycroft-core/archive/release/v18.8.4.tar.gz
Source0  : https://github.com/MycroftAI/mycroft-core/archive/release/v18.8.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mycroft-core-bin = %{version}-%{release}
Requires: mycroft-core-license = %{version}-%{release}
Requires: mycroft-core-python = %{version}-%{release}
Requires: mycroft-core-python3 = %{version}-%{release}
Requires: PyYAML
Requires: fasteners
Requires: gTTS-token
Requires: google-api-python-client
Requires: pep8
Requires: psutil
Requires: pyserial
Requires: python-dateutil
Requires: requests
Requires: six
Requires: tornado
Requires: websocket_client
BuildRequires : buildreq-distutils3

%description
/* ====================================================================
* reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
*
* 1. Redistributions of source code must retain the above copyright
*    notice, this list of conditions and the following disclaimer.
*
* 2. Redistributions in binary form must reproduce the above copyright
*    notice, this list of conditions and the following disclaimer in
*    the documentation and/or other materials provided with the
*    distribution.
*
* This work was supported in part by funding from the Defense Advanced
* Research Projects Agency and the National Science Foundation of the
* United States of America, and the CMU Sphinx Speech Consortium.
*
* THIS SOFTWARE IS PROVIDED BY ALPHA CEPHEI INC. ``AS IS'' AND
* ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
* THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
* PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL ALPHA CEPHEI INC.
* NOR ITS EMPLOYEES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
* SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
* LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
* THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
* OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*
* ====================================================================
*
*/

%package bin
Summary: bin components for the mycroft-core package.
Group: Binaries
Requires: mycroft-core-license = %{version}-%{release}

%description bin
bin components for the mycroft-core package.


%package license
Summary: license components for the mycroft-core package.
Group: Default

%description license
license components for the mycroft-core package.


%package python
Summary: python components for the mycroft-core package.
Group: Default
Requires: mycroft-core-python3 = %{version}-%{release}

%description python
python components for the mycroft-core package.


%package python3
Summary: python3 components for the mycroft-core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mycroft-core package.


%prep
%setup -q -n mycroft-core-release-v18.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541256937
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mycroft-core
cp LICENSE.md %{buildroot}/usr/share/package-licenses/mycroft-core/LICENSE.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mycroft-audio
/usr/bin/mycroft-audio-test
/usr/bin/mycroft-cli-client
/usr/bin/mycroft-echo-observer
/usr/bin/mycroft-enclosure-client
/usr/bin/mycroft-messagebus
/usr/bin/mycroft-skills
/usr/bin/mycroft-speech-client

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mycroft-core/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
