VERSION = 1.0.0
TARFILE = nc-vsock-${VERSION}.tar.gz

all: nc-vsock

rpm:
	wget -O ~/rpmbuild/SOURCES/${TARFILE} https://github.com/stefanha/nc-vsock/archive/v1.0.0.tar.gz
	rpmbuild -ba nc-vsock.spec

rpm-local:
	git archive --format tar.gz --prefix nc-vsock-${VERSION}/ --output ~/rpmbuild/SOURCES/${TARFILE} HEAD
	rpmbuild -ba nc-vsock.spec
