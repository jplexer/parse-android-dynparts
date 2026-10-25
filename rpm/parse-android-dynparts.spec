Name:       parse-android-dynparts
Version:    1.0
Release:    1
Summary:    Print dmsetup tables for Android dynamic partitions in super
License:    Apache-2.0
URL:        https://github.com/tchebb/parse-android-dynparts
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: pkgconfig(openssl)

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags}

%install
install -Dm755 build/parse-android-dynparts %{buildroot}%{_bindir}/parse-android-dynparts

%files
%{_bindir}/parse-android-dynparts
