Name:		nc-vsock
Version:	1.0.0
Release:	1%{?dist}
Summary:	netcat-like utility for AF_VSOCK

Group:		Applications/System
License:	GPLv2+
URL:		https://github.com/stefanha/nc-vsock
Source0:	nc-vsock-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
nc-vsock is a netcat-like utility for connecting over AF_VSOCK address family
and listening for incoming connections.  It supports tunneling over TCP on the
listen side.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
install -D -p -m 755 nc-vsock %{buildroot}%{_bindir}/nc-vsock

%files
%{_bindir}/nc-vsock
%doc



%changelog
* Wed Oct 19 2016 Stefan Hajnoczi <stefanha@redhat.com> 1.0.0-1
- Initial package build
