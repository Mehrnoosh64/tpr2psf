'''Wrapper for atoms.h

Generated with:
ctypesgen.py /home/piton/scr/gromacs-4.5.5/include/types/atoms.h /home/piton/scr/gromacs-4.5.5/include/types/block.h /home/piton/scr/gromacs-4.5.5/include/types/commrec.h /home/piton/scr/gromacs-4.5.5/include/types/constr.h /home/piton/scr/gromacs-4.5.5/include/types/energy.h /home/piton/scr/gromacs-4.5.5/include/types/enums.h /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h /home/piton/scr/gromacs-4.5.5/include/types/filenm.h /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h /home/piton/scr/gromacs-4.5.5/include/types/genborn.h /home/piton/scr/gromacs-4.5.5/include/types/globsig.h /home/piton/scr/gromacs-4.5.5/include/types/graph.h /home/piton/scr/gromacs-4.5.5/include/types/group.h /home/piton/scr/gromacs-4.5.5/include/types/idef.h /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h /home/piton/scr/gromacs-4.5.5/include/types/inputrec.h /home/piton/scr/gromacs-4.5.5/include/types/ishift.h /home/piton/scr/gromacs-4.5.5/include/types/iteratedconstraints.h /home/piton/scr/gromacs-4.5.5/include/types/matrix.h /home/piton/scr/gromacs-4.5.5/include/types/mdatom.h /home/piton/scr/gromacs-4.5.5/include/types/nblist.h /home/piton/scr/gromacs-4.5.5/include/types/nlistheuristics.h /home/piton/scr/gromacs-4.5.5/include/types/nrnb.h /home/piton/scr/gromacs-4.5.5/include/types/nsgrid.h /home/piton/scr/gromacs-4.5.5/include/types/ns.h /home/piton/scr/gromacs-4.5.5/include/types/oenv.h /home/piton/scr/gromacs-4.5.5/include/types/pbc.h /home/piton/scr/gromacs-4.5.5/include/types/qmmmrec.h /home/piton/scr/gromacs-4.5.5/include/types/shellfc.h /home/piton/scr/gromacs-4.5.5/include/types/simple.h /home/piton/scr/gromacs-4.5.5/include/types/state.h /home/piton/scr/gromacs-4.5.5/include/types/symtab.h /home/piton/scr/gromacs-4.5.5/include/types/topology.h /home/piton/scr/gromacs-4.5.5/include/types/trx.h -o /home/piton/devel/gmx2psf/types455.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

NULL = None # <built-in>

gmx_bool = c_int # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 85

atom_id = c_int # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 96

real = c_float # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 134

rvec = real * 3 # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 145

dvec = c_double * 3 # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 147

matrix = (real * 3) * 3 # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 149

tensor = (real * 3) * 3 # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 151

ivec = c_int * 3 # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 153

imatrix = (c_int * 3) * 3 # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 155

gmx_large_int_t = c_longlong # /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 172

enum_anon_1 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 45

eptAtom = 0 # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 45

eptNucleus = (eptAtom + 1) # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 45

eptShell = (eptNucleus + 1) # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 45

eptBond = (eptShell + 1) # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 45

eptVSite = (eptBond + 1) # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 45

eptNR = (eptVSite + 1) # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 45

# /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 59
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'm',
    'q',
    'mB',
    'qB',
    'type',
    'typeB',
    'ptype',
    'resind',
    'atomnumber',
    'elem',
]
struct_anon_2._fields_ = [
    ('m', real),
    ('q', real),
    ('mB', real),
    ('qB', real),
    ('type', c_ushort),
    ('typeB', c_ushort),
    ('ptype', c_int),
    ('resind', c_int),
    ('atomnumber', c_int),
    ('elem', c_char * 4),
]

t_atom = struct_anon_2 # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 59

# /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 68
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'name',
    'nr',
    'ic',
    'chainnum',
    'chainid',
    'rtp',
]
struct_anon_3._fields_ = [
    ('name', POINTER(POINTER(c_char))),
    ('nr', c_int),
    ('ic', c_ubyte),
    ('chainnum', c_int),
    ('chainid', c_char),
    ('rtp', POINTER(POINTER(c_char))),
]

t_resinfo = struct_anon_3 # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 68

# /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 79
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'type',
    'atomnr',
    'altloc',
    'atomnm',
    'occup',
    'bfac',
    'bAnisotropic',
    'uij',
]
struct_anon_4._fields_ = [
    ('type', c_int),
    ('atomnr', c_int),
    ('altloc', c_char),
    ('atomnm', c_char * 6),
    ('occup', real),
    ('bfac', real),
    ('bAnisotropic', gmx_bool),
    ('uij', c_int * 6),
]

t_pdbinfo = struct_anon_4 # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 79

# /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 84
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'nr',
    'nm_ind',
]
struct_anon_5._fields_ = [
    ('nr', c_int),
    ('nm_ind', POINTER(c_int)),
]

t_grps = struct_anon_5 # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 84

# /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 100
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'nr',
    'atom',
    'atomname',
    'atomtype',
    'atomtypeB',
    'nres',
    'resinfo',
    'pdbinfo',
]
struct_anon_6._fields_ = [
    ('nr', c_int),
    ('atom', POINTER(t_atom)),
    ('atomname', POINTER(POINTER(POINTER(c_char)))),
    ('atomtype', POINTER(POINTER(POINTER(c_char)))),
    ('atomtypeB', POINTER(POINTER(POINTER(c_char)))),
    ('nres', c_int),
    ('resinfo', POINTER(t_resinfo)),
    ('pdbinfo', POINTER(t_pdbinfo)),
]

t_atoms = struct_anon_6 # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 100

# /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 110
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'nr',
    'radius',
    'vol',
    'surftens',
    'gb_radius',
    'S_hct',
    'atomnumber',
]
struct_anon_7._fields_ = [
    ('nr', c_int),
    ('radius', POINTER(real)),
    ('vol', POINTER(real)),
    ('surftens', POINTER(real)),
    ('gb_radius', POINTER(real)),
    ('S_hct', POINTER(real)),
    ('atomnumber', POINTER(c_int)),
]

t_atomtypes = struct_anon_7 # /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 110

t_iatom = atom_id # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 53

enum_anon_8 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_BONDS = 0 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_G96BONDS = (F_BONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_MORSE = (F_G96BONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_CUBICBONDS = (F_MORSE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_CONNBONDS = (F_CUBICBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_HARMONIC = (F_CONNBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_FENEBONDS = (F_HARMONIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_TABBONDS = (F_FENEBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_TABBONDSNC = (F_TABBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_RESTRBONDS = (F_TABBONDSNC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_ANGLES = (F_RESTRBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_G96ANGLES = (F_ANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_CROSS_BOND_BONDS = (F_G96ANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_CROSS_BOND_ANGLES = (F_CROSS_BOND_BONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_UREY_BRADLEY = (F_CROSS_BOND_ANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_QUARTIC_ANGLES = (F_UREY_BRADLEY + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_TABANGLES = (F_QUARTIC_ANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_PDIHS = (F_TABANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_RBDIHS = (F_PDIHS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_FOURDIHS = (F_RBDIHS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_IDIHS = (F_FOURDIHS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_PIDIHS = (F_IDIHS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_TABDIHS = (F_PIDIHS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_CMAP = (F_TABDIHS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_GB12 = (F_CMAP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_GB13 = (F_GB12 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_GB14 = (F_GB13 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_GBPOL = (F_GB14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_NPSOLVATION = (F_GBPOL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_LJ14 = (F_NPSOLVATION + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_COUL14 = (F_LJ14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_LJC14_Q = (F_COUL14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_LJC_PAIRS_NB = (F_LJC14_Q + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_LJ = (F_LJC_PAIRS_NB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_BHAM = (F_LJ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_LJ_LR = (F_BHAM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_BHAM_LR = (F_LJ_LR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DISPCORR = (F_BHAM_LR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_COUL_SR = (F_DISPCORR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_COUL_LR = (F_COUL_SR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_RF_EXCL = (F_COUL_LR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_COUL_RECIP = (F_RF_EXCL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DPD = (F_COUL_RECIP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_POLARIZATION = (F_DPD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_WATER_POL = (F_POLARIZATION + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_THOLE_POL = (F_WATER_POL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_POSRES = (F_THOLE_POL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DISRES = (F_POSRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DISRESVIOL = (F_DISRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_ORIRES = (F_DISRESVIOL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_ORIRESDEV = (F_ORIRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_ANGRES = (F_ORIRESDEV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_ANGRESZ = (F_ANGRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DIHRES = (F_ANGRESZ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DIHRESVIOL = (F_DIHRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_CONSTR = (F_DIHRESVIOL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_CONSTRNC = (F_CONSTR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_SETTLE = (F_CONSTRNC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITE2 = (F_SETTLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITE3 = (F_VSITE2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITE3FD = (F_VSITE3 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITE3FAD = (F_VSITE3FD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITE3OUT = (F_VSITE3FAD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITE4FD = (F_VSITE3OUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITE4FDN = (F_VSITE4FD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VSITEN = (F_VSITE4FDN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_COM_PULL = (F_VSITEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_EQM = (F_COM_PULL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_EPOT = (F_EQM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_EKIN = (F_EPOT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_ETOT = (F_EKIN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_ECONSERVED = (F_ETOT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_TEMP = (F_ECONSERVED + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_VTEMP = (F_TEMP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_PDISPCORR = (F_VTEMP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_PRES = (F_PDISPCORR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DVDL = (F_PRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DKDL = (F_DVDL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_DHDL_CON = (F_DKDL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

F_NRE = (F_DHDL_CON + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 57

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 148
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'a',
    'b',
    'c',
]
struct_anon_9._fields_ = [
    ('a', real),
    ('b', real),
    ('c', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 149
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'rA',
    'krA',
    'rB',
    'krB',
]
struct_anon_10._fields_ = [
    ('rA', real),
    ('krA', real),
    ('rB', real),
    ('krB', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 150
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'lowA',
    'up1A',
    'up2A',
    'kA',
    'lowB',
    'up1B',
    'up2B',
    'kB',
]
struct_anon_11._fields_ = [
    ('lowA', real),
    ('up1A', real),
    ('up2A', real),
    ('kA', real),
    ('lowB', real),
    ('up1B', real),
    ('up2B', real),
    ('kB', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 152
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'b0',
    'kb',
    'kcub',
]
struct_anon_12._fields_ = [
    ('b0', real),
    ('kb', real),
    ('kcub', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 153
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'bm',
    'kb',
]
struct_anon_13._fields_ = [
    ('bm', real),
    ('kb', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 154
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'r1e',
    'r2e',
    'krr',
]
struct_anon_14._fields_ = [
    ('r1e', real),
    ('r2e', real),
    ('krr', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 155
class struct_anon_15(Structure):
    pass

struct_anon_15.__slots__ = [
    'r1e',
    'r2e',
    'r3e',
    'krt',
]
struct_anon_15._fields_ = [
    ('r1e', real),
    ('r2e', real),
    ('r3e', real),
    ('krt', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 156
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'theta',
    'ktheta',
    'r13',
    'kUB',
]
struct_anon_16._fields_ = [
    ('theta', real),
    ('ktheta', real),
    ('r13', real),
    ('kUB', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 157
class struct_anon_17(Structure):
    pass

struct_anon_17.__slots__ = [
    'theta',
    'c',
]
struct_anon_17._fields_ = [
    ('theta', real),
    ('c', real * 5),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 158
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'alpha',
]
struct_anon_18._fields_ = [
    ('alpha', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 159
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'al_x',
    'al_y',
    'al_z',
    'rOH',
    'rHH',
    'rOD',
]
struct_anon_19._fields_ = [
    ('al_x', real),
    ('al_y', real),
    ('al_z', real),
    ('rOH', real),
    ('rHH', real),
    ('rOD', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 160
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'a',
    'alpha1',
    'alpha2',
    'rfac',
]
struct_anon_20._fields_ = [
    ('a', real),
    ('alpha1', real),
    ('alpha2', real),
    ('rfac', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 161
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'c6',
    'c12',
]
struct_anon_21._fields_ = [
    ('c6', real),
    ('c12', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 162
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'c6A',
    'c12A',
    'c6B',
    'c12B',
]
struct_anon_22._fields_ = [
    ('c6A', real),
    ('c12A', real),
    ('c6B', real),
    ('c12B', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 163
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'fqq',
    'qi',
    'qj',
    'c6',
    'c12',
]
struct_anon_23._fields_ = [
    ('fqq', real),
    ('qi', real),
    ('qj', real),
    ('c6', real),
    ('c12', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 164
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'qi',
    'qj',
    'c6',
    'c12',
]
struct_anon_24._fields_ = [
    ('qi', real),
    ('qj', real),
    ('c6', real),
    ('c12', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 169
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'phiA',
    'cpA',
    'mult',
    'phiB',
    'cpB',
]
struct_anon_25._fields_ = [
    ('phiA', real),
    ('cpA', real),
    ('mult', c_int),
    ('phiB', real),
    ('cpB', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 170
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'dA',
    'dB',
]
struct_anon_26._fields_ = [
    ('dA', real),
    ('dB', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 174
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'doh',
    'dhh',
]
struct_anon_27._fields_ = [
    ('doh', real),
    ('dhh', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 176
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'b0',
    'cb',
    'beta',
]
struct_anon_28._fields_ = [
    ('b0', real),
    ('cb', real),
    ('beta', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 177
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'pos0A',
    'fcA',
    'pos0B',
    'fcB',
]
struct_anon_29._fields_ = [
    ('pos0A', real * 3),
    ('fcA', real * 3),
    ('pos0B', real * 3),
    ('fcB', real * 3),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 178
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'rbcA',
    'rbcB',
]
struct_anon_30._fields_ = [
    ('rbcA', real * 6),
    ('rbcB', real * 6),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 179
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
]
struct_anon_31._fields_ = [
    ('a', real),
    ('b', real),
    ('c', real),
    ('d', real),
    ('e', real),
    ('f', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 180
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'n',
    'a',
]
struct_anon_32._fields_ = [
    ('n', c_int),
    ('a', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 182
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'low',
    'up1',
    'up2',
    'kfac',
    'type',
    'label',
    'npair',
]
struct_anon_33._fields_ = [
    ('low', real),
    ('up1', real),
    ('up2', real),
    ('kfac', real),
    ('type', c_int),
    ('label', c_int),
    ('npair', c_int),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 183
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'phi',
    'dphi',
    'kfac',
    'label',
    'power',
]
struct_anon_34._fields_ = [
    ('phi', real),
    ('dphi', real),
    ('kfac', real),
    ('label', c_int),
    ('power', c_int),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 184
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'ex',
    'power',
    'label',
    'c',
    'obs',
    'kfac',
]
struct_anon_35._fields_ = [
    ('ex', c_int),
    ('power', c_int),
    ('label', c_int),
    ('c', real),
    ('obs', real),
    ('kfac', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 185
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'table',
    'kA',
    'kB',
]
struct_anon_36._fields_ = [
    ('table', c_int),
    ('kA', real),
    ('kB', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 186
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'sar',
    'st',
    'pi',
    'gbr',
    'bmlt',
]
struct_anon_37._fields_ = [
    ('sar', real),
    ('st', real),
    ('pi', real),
    ('gbr', real),
    ('bmlt', real),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 187
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'cmapA',
    'cmapB',
]
struct_anon_38._fields_ = [
    ('cmapA', c_int),
    ('cmapB', c_int),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 188
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'buf',
]
struct_anon_39._fields_ = [
    ('buf', real * 12),
]

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 189
class union_anon_40(Union):
    pass

union_anon_40.__slots__ = [
    'bham',
    'harmonic',
    'restraint',
    'cubic',
    'fene',
    'cross_bb',
    'cross_ba',
    'u_b',
    'qangle',
    'polarize',
    'wpol',
    'thole',
    'lj',
    'lj14',
    'ljc14',
    'ljcnb',
    'pdihs',
    'constr',
    'settle',
    'morse',
    'posres',
    'rbdihs',
    'vsite',
    'vsiten',
    'disres',
    'dihres',
    'orires',
    'tab',
    'gb',
    'cmap',
    'generic',
]
union_anon_40._fields_ = [
    ('bham', struct_anon_9),
    ('harmonic', struct_anon_10),
    ('restraint', struct_anon_11),
    ('cubic', struct_anon_12),
    ('fene', struct_anon_13),
    ('cross_bb', struct_anon_14),
    ('cross_ba', struct_anon_15),
    ('u_b', struct_anon_16),
    ('qangle', struct_anon_17),
    ('polarize', struct_anon_18),
    ('wpol', struct_anon_19),
    ('thole', struct_anon_20),
    ('lj', struct_anon_21),
    ('lj14', struct_anon_22),
    ('ljc14', struct_anon_23),
    ('ljcnb', struct_anon_24),
    ('pdihs', struct_anon_25),
    ('constr', struct_anon_26),
    ('settle', struct_anon_27),
    ('morse', struct_anon_28),
    ('posres', struct_anon_29),
    ('rbdihs', struct_anon_30),
    ('vsite', struct_anon_31),
    ('vsiten', struct_anon_32),
    ('disres', struct_anon_33),
    ('dihres', struct_anon_34),
    ('orires', struct_anon_35),
    ('tab', struct_anon_36),
    ('gb', struct_anon_37),
    ('cmap', struct_anon_38),
    ('generic', struct_anon_39),
]

t_iparams = union_anon_40 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 189

t_functype = c_int # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 191

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 205
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'nr',
    'nr_nonperturbed',
    'iatoms',
    'nalloc',
]
struct_anon_41._fields_ = [
    ('nr', c_int),
    ('nr_nonperturbed', c_int),
    ('iatoms', POINTER(t_iatom)),
    ('nalloc', c_int),
]

t_ilist = struct_anon_41 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 205

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 230
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'cmap',
]
struct_anon_42._fields_ = [
    ('cmap', POINTER(real)),
]

cmapdata_t = struct_anon_42 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 230

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 237
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'ngrid',
    'grid_spacing',
    'cmapdata',
]
struct_anon_43._fields_ = [
    ('ngrid', c_int),
    ('grid_spacing', c_int),
    ('cmapdata', POINTER(cmapdata_t)),
]

gmx_cmap_t = struct_anon_43 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 237

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 249
class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    'ntypes',
    'atnr',
    'functype',
    'iparams',
    'reppow',
    'fudgeQQ',
    'cmap_grid',
]
struct_anon_44._fields_ = [
    ('ntypes', c_int),
    ('atnr', c_int),
    ('functype', POINTER(t_functype)),
    ('iparams', POINTER(t_iparams)),
    ('reppow', c_double),
    ('fudgeQQ', real),
    ('cmap_grid', gmx_cmap_t),
]

gmx_ffparams_t = struct_anon_44 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 249

enum_anon_45 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 251

ilsortUNKNOWN = 0 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 251

ilsortNO_FE = (ilsortUNKNOWN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 251

ilsortFE_UNSORTED = (ilsortNO_FE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 251

ilsortFE_SORTED = (ilsortFE_UNSORTED + 1) # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 251

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 268
class struct_anon_46(Structure):
    pass

struct_anon_46.__slots__ = [
    'ntypes',
    'atnr',
    'functype',
    'iparams',
    'fudgeQQ',
    'cmap_grid',
    'iparams_posres',
    'iparams_posres_nalloc',
    'il',
    'ilsort',
]
struct_anon_46._fields_ = [
    ('ntypes', c_int),
    ('atnr', c_int),
    ('functype', POINTER(t_functype)),
    ('iparams', POINTER(t_iparams)),
    ('fudgeQQ', real),
    ('cmap_grid', gmx_cmap_t),
    ('iparams_posres', POINTER(t_iparams)),
    ('iparams_posres_nalloc', c_int),
    ('il', t_ilist * F_NRE),
    ('ilsort', c_int),
]

t_idef = struct_anon_46 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 268

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 306
class struct_anon_47(Structure):
    pass

struct_anon_47.__slots__ = [
    'n',
    'scale',
    'tab',
]
struct_anon_47._fields_ = [
    ('n', c_int),
    ('scale', real),
    ('tab', POINTER(real)),
]

bondedtable_t = struct_anon_47 # /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 306

# /home/piton/scr/gromacs-4.5.5/include/types/block.h: 57
class struct_anon_48(Structure):
    pass

struct_anon_48.__slots__ = [
    'nr',
    'index',
    'nalloc_index',
]
struct_anon_48._fields_ = [
    ('nr', c_int),
    ('index', POINTER(atom_id)),
    ('nalloc_index', c_int),
]

t_block = struct_anon_48 # /home/piton/scr/gromacs-4.5.5/include/types/block.h: 57

# /home/piton/scr/gromacs-4.5.5/include/types/block.h: 71
class struct_anon_49(Structure):
    pass

struct_anon_49.__slots__ = [
    'nr',
    'index',
    'nra',
    'a',
    'nalloc_index',
    'nalloc_a',
]
struct_anon_49._fields_ = [
    ('nr', c_int),
    ('index', POINTER(atom_id)),
    ('nra', c_int),
    ('a', POINTER(atom_id)),
    ('nalloc_index', c_int),
    ('nalloc_a', c_int),
]

t_blocka = struct_anon_49 # /home/piton/scr/gromacs-4.5.5/include/types/block.h: 71

MPI_Comm = POINTER(None) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 45

MPI_Request = POINTER(None) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 46

MPI_Group = POINTER(None) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 47

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 61
class struct_gmx_domdec_master(Structure):
    pass

gmx_domdec_master_p_t = POINTER(struct_gmx_domdec_master) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 61

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 71
class struct_anon_50(Structure):
    pass

struct_anon_50.__slots__ = [
    'j0',
    'j1',
    'cg1',
    'jcg0',
    'jcg1',
    'shift0',
    'shift1',
]
struct_anon_50._fields_ = [
    ('j0', c_int),
    ('j1', c_int),
    ('cg1', c_int),
    ('jcg0', c_int),
    ('jcg1', c_int),
    ('shift0', ivec),
    ('shift1', ivec),
]

gmx_domdec_ns_ranges_t = struct_anon_50 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 71

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 84
class struct_anon_51(Structure):
    pass

struct_anon_51.__slots__ = [
    'n',
    'shift',
    'cg_range',
    'nizone',
    'izone',
]
struct_anon_51._fields_ = [
    ('n', c_int),
    ('shift', ivec * 8),
    ('cg_range', c_int * (8 + 1)),
    ('nizone', c_int),
    ('izone', gmx_domdec_ns_ranges_t * 4),
]

gmx_domdec_zones_t = struct_anon_51 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 84

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 86
class struct_gmx_ga2la(Structure):
    pass

gmx_ga2la_t = POINTER(struct_gmx_ga2la) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 86

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 88
class struct_gmx_reverse_top(Structure):
    pass

gmx_reverse_top_p_t = POINTER(struct_gmx_reverse_top) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 88

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 90
class struct_gmx_domdec_constraints(Structure):
    pass

gmx_domdec_constraints_p_t = POINTER(struct_gmx_domdec_constraints) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 90

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 92
class struct_gmx_domdec_specat_comm(Structure):
    pass

gmx_domdec_specat_comm_p_t = POINTER(struct_gmx_domdec_specat_comm) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 92

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 94
class struct_gmx_domdec_comm(Structure):
    pass

gmx_domdec_comm_p_t = POINTER(struct_gmx_domdec_comm) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 94

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 96
class struct_gmx_pme_comm_n_box(Structure):
    pass

gmx_pme_comm_n_box_p_t = POINTER(struct_gmx_pme_comm_n_box) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 96

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 110
class struct_anon_52(Structure):
    pass

struct_anon_52.__slots__ = [
    'npbcdim',
    'nboundeddim',
    'box0',
    'box_size',
    'tric_dir',
    'skew_fac',
    'v',
    'normal',
]
struct_anon_52._fields_ = [
    ('npbcdim', c_int),
    ('nboundeddim', c_int),
    ('box0', rvec),
    ('box_size', rvec),
    ('tric_dir', ivec),
    ('skew_fac', rvec),
    ('v', (rvec * 3) * 3),
    ('normal', rvec * 3),
]

gmx_ddbox_t = struct_anon_52 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 110

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 127
class struct_anon_53(Structure):
    pass

struct_anon_53.__slots__ = [
    'ibuf',
    'ibuf_alloc',
    'libuf',
    'libuf_alloc',
    'fbuf',
    'fbuf_alloc',
    'dbuf',
    'dbuf_alloc',
]
struct_anon_53._fields_ = [
    ('ibuf', POINTER(c_int)),
    ('ibuf_alloc', c_int),
    ('libuf', POINTER(gmx_large_int_t)),
    ('libuf_alloc', c_int),
    ('fbuf', POINTER(c_float)),
    ('fbuf_alloc', c_int),
    ('dbuf', POINTER(c_double)),
    ('dbuf_alloc', c_int),
]

mpi_in_place_buf_t = struct_anon_53 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 127

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 221
class struct_anon_54(Structure):
    pass

struct_anon_54.__slots__ = [
    'nnodes',
    'mpi_comm_all',
    'bSendRecv2',
    'ci',
    'rank',
    'master_ci',
    'masterrank',
    'pme_nodeid',
    'pme_receive_vir_ener',
    'cnb',
    'nreq_pme',
    'req_pme',
    'nc',
    'ndim',
    'dim',
    'bGridJump',
    'npbcdim',
    'bScrewPBC',
    'neighbor',
    'ma',
    'bInterCGcons',
    'reverse_top',
    'nbonded_global',
    'nbonded_local',
    'n_intercg_excl',
    'ga2la_vsite',
    'vsite_comm',
    'constraints',
    'constraint_comm',
    'ncg_home',
    'ncg_tot',
    'index_gl',
    'cgindex',
    'cg_nalloc',
    'la2lc',
    'la2lc_nalloc',
    'nat_home',
    'nat_tot',
    'gatindex',
    'gatindex_nalloc',
    'ga2la',
    'comm',
    'ddp_count',
    'pme_recv_f_alloc',
    'pme_recv_f_buf',
]
struct_anon_54._fields_ = [
    ('nnodes', c_int),
    ('mpi_comm_all', MPI_Comm),
    ('bSendRecv2', gmx_bool),
    ('ci', ivec),
    ('rank', c_int),
    ('master_ci', ivec),
    ('masterrank', c_int),
    ('pme_nodeid', c_int),
    ('pme_receive_vir_ener', gmx_bool),
    ('cnb', gmx_pme_comm_n_box_p_t),
    ('nreq_pme', c_int),
    ('req_pme', MPI_Request * 4),
    ('nc', ivec),
    ('ndim', c_int),
    ('dim', ivec),
    ('bGridJump', gmx_bool),
    ('npbcdim', c_int),
    ('bScrewPBC', gmx_bool),
    ('neighbor', (c_int * 2) * 3),
    ('ma', gmx_domdec_master_p_t),
    ('bInterCGcons', gmx_bool),
    ('reverse_top', gmx_reverse_top_p_t),
    ('nbonded_global', c_int),
    ('nbonded_local', c_int),
    ('n_intercg_excl', c_int),
    ('ga2la_vsite', POINTER(c_int)),
    ('vsite_comm', gmx_domdec_specat_comm_p_t),
    ('constraints', gmx_domdec_constraints_p_t),
    ('constraint_comm', gmx_domdec_specat_comm_p_t),
    ('ncg_home', c_int),
    ('ncg_tot', c_int),
    ('index_gl', POINTER(c_int)),
    ('cgindex', POINTER(c_int)),
    ('cg_nalloc', c_int),
    ('la2lc', POINTER(c_int)),
    ('la2lc_nalloc', c_int),
    ('nat_home', c_int),
    ('nat_tot', c_int),
    ('gatindex', POINTER(c_int)),
    ('gatindex_nalloc', c_int),
    ('ga2la', gmx_ga2la_t),
    ('comm', gmx_domdec_comm_p_t),
    ('ddp_count', gmx_large_int_t),
    ('pme_recv_f_alloc', c_int),
    ('pme_recv_f_buf', POINTER(rvec)),
]

gmx_domdec_t = struct_anon_54 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 221

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 223
class struct_gmx_partdec(Structure):
    pass

gmx_partdec_p_t = POINTER(struct_gmx_partdec) # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 223

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 233
class struct_anon_55(Structure):
    pass

struct_anon_55.__slots__ = [
    'nsim',
    'sim',
    'mpi_group_masters',
    'mpi_comm_masters',
    'mpb',
]
struct_anon_55._fields_ = [
    ('nsim', c_int),
    ('sim', c_int),
    ('mpi_group_masters', MPI_Group),
    ('mpi_comm_masters', MPI_Comm),
    ('mpb', POINTER(mpi_in_place_buf_t)),
]

gmx_multisim_t = struct_anon_55 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 233

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 244
class struct_anon_56(Structure):
    pass

struct_anon_56.__slots__ = [
    'bUse',
    'comm_intra',
    'rank_intra',
    'comm_inter',
]
struct_anon_56._fields_ = [
    ('bUse', c_int),
    ('comm_intra', MPI_Comm),
    ('rank_intra', c_int),
    ('comm_inter', MPI_Comm),
]

gmx_nodecomm_t = struct_anon_56 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 244

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 248
class struct_anon_57(Structure):
    pass

struct_anon_57.__slots__ = [
    'dummy',
]
struct_anon_57._fields_ = [
    ('dummy', c_int),
]

gmx_commrec_thread_t = struct_anon_57 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 248

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 284
class struct_anon_58(Structure):
    pass

struct_anon_58.__slots__ = [
    'sim_nodeid',
    'nnodes',
    'npmenodes',
    'nodeid',
    'mpi_comm_mysim',
    'mpi_comm_mygroup',
    'nc',
    'dd',
    'pd',
    'duty',
    'ms',
    'mpb',
]
struct_anon_58._fields_ = [
    ('sim_nodeid', c_int),
    ('nnodes', c_int),
    ('npmenodes', c_int),
    ('nodeid', c_int),
    ('mpi_comm_mysim', MPI_Comm),
    ('mpi_comm_mygroup', MPI_Comm),
    ('nc', gmx_nodecomm_t),
    ('dd', POINTER(gmx_domdec_t)),
    ('pd', gmx_partdec_p_t),
    ('duty', c_int),
    ('ms', POINTER(gmx_multisim_t)),
    ('mpb', POINTER(mpi_in_place_buf_t)),
]

t_commrec = struct_anon_58 # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 284

# /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 44
class struct_gmx_lincsdata(Structure):
    pass

gmx_lincsdata_t = POINTER(struct_gmx_lincsdata) # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 44

# /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 47
class struct_gmx_shakedata(Structure):
    pass

gmx_shakedata_t = POINTER(struct_gmx_shakedata) # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 47

# /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 50
class struct_gmx_settledata(Structure):
    pass

gmx_settledata_t = POINTER(struct_gmx_settledata) # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 50

# /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 53
class struct_gmx_constr(Structure):
    pass

gmx_constr_t = POINTER(struct_gmx_constr) # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 53

# /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 56
class struct_gmx_edsam(Structure):
    pass

gmx_edsam_t = POINTER(struct_gmx_edsam) # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 56

# /home/piton/scr/gromacs-4.5.5/include/types/energy.h: 46
class struct_anon_59(Structure):
    pass

struct_anon_59.__slots__ = [
    'e',
    'eav',
    'esum',
]
struct_anon_59._fields_ = [
    ('e', real),
    ('eav', c_double),
    ('esum', c_double),
]

t_energy = struct_anon_59 # /home/piton/scr/gromacs-4.5.5/include/types/energy.h: 46

enum_anon_60 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 42

epbcXYZ = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 42

epbcNONE = (epbcXYZ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 42

epbcXY = (epbcNONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 42

epbcSCREW = (epbcXY + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 42

epbcNR = (epbcSCREW + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 42

enum_anon_61 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcBERENDSEN = (etcNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcNOSEHOOVER = (etcBERENDSEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcYES = (etcNOSEHOOVER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcANDERSEN = (etcYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcANDERSENINTERVAL = (etcANDERSEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcVRESCALE = (etcANDERSENINTERVAL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

etcNR = (etcVRESCALE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 46

enum_anon_62 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 50

epcNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 50

epcBERENDSEN = (epcNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 50

epcPARRINELLORAHMAN = (epcBERENDSEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 50

epcISOTROPIC = (epcPARRINELLORAHMAN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 50

epcMTTK = (epcISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 50

epcNR = (epcMTTK + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 50

enum_anon_63 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtNONE = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtNHC = (etrtNONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtBAROV = (etrtNHC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtBARONHC = (etrtBAROV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtNHC2 = (etrtBARONHC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtBAROV2 = (etrtNHC2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtBARONHC2 = (etrtBAROV2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtVELOCITY1 = (etrtBARONHC2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtVELOCITY2 = (etrtVELOCITY1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtPOSITION = (etrtVELOCITY2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtSKIPALL = (etrtPOSITION + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

etrtNR = (etrtSKIPALL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 55

enum_anon_64 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 61

ettTSEQ0 = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 61

ettTSEQ1 = (ettTSEQ0 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 61

ettTSEQ2 = (ettTSEQ1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 61

ettTSEQ3 = (ettTSEQ2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 61

ettTSEQ4 = (ettTSEQ3 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 61

ettTSEQMAX = (ettTSEQ4 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 61

enum_anon_65 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 65

epctISOTROPIC = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 65

epctSEMIISOTROPIC = (epctISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 65

epctANISOTROPIC = (epctSEMIISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 65

epctSURFACETENSION = (epctANISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 65

epctNR = (epctSURFACETENSION + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 65

enum_anon_66 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 70

erscNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 70

erscALL = (erscNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 70

erscCOM = (erscALL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 70

erscNR = (erscCOM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 70

enum_anon_67 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelCUT = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelRF = (eelCUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelGRF = (eelRF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelPME = (eelGRF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelEWALD = (eelPME + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelPPPM = (eelEWALD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelPOISSON = (eelPPPM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelSWITCH = (eelPOISSON + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelSHIFT = (eelSWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelUSER = (eelSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelGB_NOTUSED = (eelUSER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelRF_NEC = (eelGB_NOTUSED + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelENCADSHIFT = (eelRF_NEC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelPMEUSER = (eelENCADSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelPMESWITCH = (eelPMEUSER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelPMEUSERSWITCH = (eelPMESWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelRF_ZERO = (eelPMEUSERSWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

eelNR = (eelRF_ZERO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 79

enum_anon_68 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 86

eewg3D = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 86

eewg3DC = (eewg3D + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 86

eewgNR = (eewg3DC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 86

enum_anon_69 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 101

evdwCUT = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 101

evdwSWITCH = (evdwCUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 101

evdwSHIFT = (evdwSWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 101

evdwUSER = (evdwSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 101

evdwENCADSHIFT = (evdwUSER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 101

evdwNR = (evdwENCADSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 101

enum_anon_70 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 111

ensGRID = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 111

ensSIMPLE = (ensGRID + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 111

ensNR = (ensSIMPLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 111

enum_anon_71 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiMD = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiSteep = (eiMD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiCG = (eiSteep + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiBD = (eiCG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiSD2 = (eiBD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiNM = (eiSD2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiLBFGS = (eiNM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiTPI = (eiLBFGS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiTPIC = (eiTPI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiSD1 = (eiTPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiVV = (eiSD1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiVVAK = (eiVV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

eiNR = (eiVVAK + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 118

enum_anon_72 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 131

econtLINCS = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 131

econtSHAKE = (econtLINCS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 131

econtNR = (econtSHAKE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 131

enum_anon_73 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 135

edrNone = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 135

edrSimple = (edrNone + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 135

edrEnsemble = (edrSimple + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 135

edrNR = (edrEnsemble + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 135

enum_anon_74 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 139

edrwConservative = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 139

edrwEqual = (edrwConservative + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 139

edrwNR = (edrwEqual + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 139

enum_anon_75 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 144

eCOMB_NONE = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 144

eCOMB_GEOMETRIC = (eCOMB_NONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 144

eCOMB_ARITHMETIC = (eCOMB_GEOMETRIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 144

eCOMB_GEOM_SIG_EPS = (eCOMB_ARITHMETIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 144

eCOMB_NR = (eCOMB_GEOM_SIG_EPS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 144

enum_anon_76 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 149

eNBF_NONE = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 149

eNBF_LJ = (eNBF_NONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 149

eNBF_BHAM = (eNBF_LJ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 149

eNBF_NR = (eNBF_BHAM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 149

enum_anon_77 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 154

efepNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 154

efepYES = (efepNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 154

efepNR = (efepYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 154

enum_anon_78 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 159

sepdhdlfileYES = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 159

sepdhdlfileNO = (sepdhdlfileYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 159

sepdhdlfileNR = (sepdhdlfileNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 159

enum_anon_79 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 166

dhdlderivativesYES = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 166

dhdlderivativesNO = (dhdlderivativesYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 166

dhdlderivativesNR = (dhdlderivativesNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 166

enum_anon_80 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 173

esolNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 173

esolSPC = (esolNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 173

esolTIP4P = (esolSPC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 173

esolNR = (esolTIP4P + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 173

enum_anon_81 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 178

edispcNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 178

edispcEnerPres = (edispcNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 178

edispcEner = (edispcEnerPres + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 178

edispcAllEnerPres = (edispcEner + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 178

edispcAllEner = (edispcAllEnerPres + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 178

edispcNR = (edispcAllEner + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 178

enum_anon_82 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 183

eshellCSH = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 183

eshellBASH = (eshellCSH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 183

eshellZSH = (eshellBASH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 183

eshellNR = (eshellZSH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 183

enum_anon_83 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 188

ecmLINEAR = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 188

ecmANGULAR = (ecmLINEAR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 188

ecmNO = (ecmANGULAR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 188

ecmNR = (ecmNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 188

enum_anon_84 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 193

eannNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 193

eannSINGLE = (eannNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 193

eannPERIODIC = (eannSINGLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 193

eannNR = (eannPERIODIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 193

enum_anon_85 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 198

eisNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 198

eisGBSA = (eisNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 198

eisNR = (eisGBSA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 198

enum_anon_86 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 203

egbSTILL = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 203

egbHCT = (egbSTILL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 203

egbOBC = (egbHCT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 203

egbNR = (egbOBC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 203

enum_anon_87 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 207

esaAPPROX = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 207

esaNO = (esaAPPROX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 207

esaSTILL = (esaNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 207

esaNR = (esaSTILL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 207

enum_anon_88 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 212

ewt93 = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 212

ewt104 = (ewt93 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 212

ewtTABLE = (ewt104 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 212

ewt126 = (ewtTABLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 212

ewtNR = (ewt126 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 212

enum_anon_89 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 217

epullNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 217

epullUMBRELLA = (epullNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 217

epullCONSTRAINT = (epullUMBRELLA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 217

epullCONST_F = (epullCONSTRAINT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 217

epullNR = (epullCONST_F + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 217

enum_anon_90 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 221

epullgDIST = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 221

epullgDIR = (epullgDIST + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 221

epullgCYL = (epullgDIR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 221

epullgPOS = (epullgCYL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 221

epullgDIRPBC = (epullgPOS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 221

epullgNR = (epullgDIRPBC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 221

enum_anon_91 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodAM1 = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodPM3 = (eQMmethodAM1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodRHF = (eQMmethodPM3 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodUHF = (eQMmethodRHF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodDFT = (eQMmethodUHF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodB3LYP = (eQMmethodDFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodMP2 = (eQMmethodB3LYP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodCASSCF = (eQMmethodMP2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodB3LYPLAN = (eQMmethodCASSCF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodDIRECT = (eQMmethodB3LYPLAN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

eQMmethodNR = (eQMmethodDIRECT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 228

enum_anon_92 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasisSTO3G = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasisSTO3G2 = (eQMbasisSTO3G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis321G = (eQMbasisSTO3G2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis321Gp = (eQMbasis321G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis321dGp = (eQMbasis321Gp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis621G = (eQMbasis321dGp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis631G = (eQMbasis621G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis631Gp = (eQMbasis631G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis631dGp = (eQMbasis631Gp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasis6311G = (eQMbasis631dGp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

eQMbasisNR = (eQMbasis6311G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 234

enum_anon_93 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 241

eQMMMschemenormal = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 241

eQMMMschemeoniom = (eQMMMschemenormal + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 241

eQMMMschemeNR = (eQMMMschemeoniom + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 241

enum_anon_94 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 245

eMultentOptName = 0 # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 245

eMultentOptNo = (eMultentOptName + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 245

eMultentOptLast = (eMultentOptNo + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 245

eMultentOptNR = (eMultentOptLast + 1) # /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 245

rvec5 = real * 5 # /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h: 42

# /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h: 66
class struct_anon_95(Structure):
    pass

struct_anon_95.__slots__ = [
    'dr_weighting',
    'dr_bMixed',
    'dr_fc',
    'dr_tau',
    'ETerm',
    'ETerm1',
    'exp_min_t_tau',
    'nres',
    'npair',
    'sumviol',
    'rt',
    'rm3tav',
    'Rtl_6',
    'Rt_6',
    'Rtav_6',
    'nsystems',
    'mpi_comm_ensemble',
]
struct_anon_95._fields_ = [
    ('dr_weighting', c_int),
    ('dr_bMixed', gmx_bool),
    ('dr_fc', real),
    ('dr_tau', real),
    ('ETerm', real),
    ('ETerm1', real),
    ('exp_min_t_tau', real),
    ('nres', c_int),
    ('npair', c_int),
    ('sumviol', real),
    ('rt', POINTER(real)),
    ('rm3tav', POINTER(real)),
    ('Rtl_6', POINTER(real)),
    ('Rt_6', POINTER(real)),
    ('Rtav_6', POINTER(real)),
    ('nsystems', c_int),
    ('mpi_comm_ensemble', MPI_Comm),
]

t_disresdata = struct_anon_95 # /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h: 66

# /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h: 98
class struct_anon_96(Structure):
    pass

struct_anon_96.__slots__ = [
    'fc',
    'edt',
    'edt_1',
    'exp_min_t_tau',
    'nr',
    'nex',
    'nref',
    'mref',
    'xref',
    'xtmp',
    'R',
    'S',
    'Dinsl',
    'Dins',
    'Dtav',
    'oinsl',
    'oins',
    'otav',
    'rmsdev',
    'tmp',
    'TMP',
    'eig',
    'M',
    'eig_diag',
    'v',
]
struct_anon_96._fields_ = [
    ('fc', real),
    ('edt', real),
    ('edt_1', real),
    ('exp_min_t_tau', real),
    ('nr', c_int),
    ('nex', c_int),
    ('nref', c_int),
    ('mref', POINTER(real)),
    ('xref', POINTER(rvec)),
    ('xtmp', POINTER(rvec)),
    ('R', matrix),
    ('S', POINTER(tensor)),
    ('Dinsl', POINTER(rvec5)),
    ('Dins', POINTER(rvec5)),
    ('Dtav', POINTER(rvec5)),
    ('oinsl', POINTER(real)),
    ('oins', POINTER(real)),
    ('otav', POINTER(real)),
    ('rmsdev', real),
    ('tmp', POINTER(rvec5)),
    ('TMP', POINTER(POINTER(POINTER(real)))),
    ('eig', POINTER(real)),
    ('M', POINTER(POINTER(c_double))),
    ('eig_diag', POINTER(c_double)),
    ('v', POINTER(POINTER(c_double))),
]

t_oriresdata = struct_anon_96 # /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h: 98

# /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h: 115
class struct_anon_97(Structure):
    pass

struct_anon_97.__slots__ = [
    'bondtab',
    'angletab',
    'dihtab',
    'disres',
    'orires',
    'dihre_fc',
]
struct_anon_97._fields_ = [
    ('bondtab', POINTER(bondedtable_t)),
    ('angletab', POINTER(bondedtable_t)),
    ('dihtab', POINTER(bondedtable_t)),
    ('disres', t_disresdata),
    ('orires', t_oriresdata),
    ('dihre_fc', real),
]

t_fcdata = struct_anon_97 # /home/piton/scr/gromacs-4.5.5/include/types/fcdata.h: 115

enum_anon_98 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efMDP = 0 # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efGCT = (efMDP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTRX = (efGCT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTRO = (efTRX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTRN = (efTRO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTRR = (efTRN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTRJ = (efTRR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efXTC = (efTRJ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efG87 = (efXTC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efEDR = (efG87 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efSTX = (efEDR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efSTO = (efSTX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efGRO = (efSTO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efG96 = (efGRO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efPDB = (efG96 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efBRK = (efPDB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efENT = (efBRK + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efESP = (efENT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efPQR = (efESP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efXYZ = (efPQR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efCPT = (efXYZ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efLOG = (efCPT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efXVG = (efLOG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efOUT = (efXVG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efNDX = (efOUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTOP = (efNDX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efITP = (efTOP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTPX = (efITP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTPS = (efTPX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTPR = (efTPS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTPA = (efTPR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTPB = (efTPA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efTEX = (efTPB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efRTP = (efTEX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efATP = (efRTP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efHDB = (efATP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efDAT = (efHDB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efDLG = (efDAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efMAP = (efDLG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efEPS = (efMAP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efMAT = (efEPS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efM2P = (efMAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efMTX = (efM2P + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efEDI = (efMTX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efEDO = (efEDI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efHAT = (efEDO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efCUB = (efHAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efXPM = (efCUB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efRND = (efXPM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

efNR = (efRND + 1) # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 42

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 71
class struct_anon_99(Structure):
    pass

struct_anon_99.__slots__ = [
    'ftp',
    'opt',
    'fn',
    'flag',
    'nfiles',
    'fns',
]
struct_anon_99._fields_ = [
    ('ftp', c_int),
    ('opt', String),
    ('fn', String),
    ('flag', c_ulong),
    ('nfiles', c_int),
    ('fns', POINTER(POINTER(c_char))),
]

t_filenm = struct_anon_99 # /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 71

# /home/piton/scr/gromacs-4.5.5/include/types/nsgrid.h: 72
class struct_anon_100(Structure):
    pass

struct_anon_100.__slots__ = [
    'nr',
    'nboundeddim',
    'npbcdim',
    'ncg_ideal',
    'n',
    'ncells',
    'cells_nalloc',
    'ncpddc',
    'cell_size',
    'cell_offset',
    'cell_index',
    'index',
    'nra',
    'icg0',
    'icg1',
    'os0',
    'os1',
    'a',
    'nr_alloc',
    'dcx2',
    'dcy2',
    'dcz2',
    'dc_nalloc',
]
struct_anon_100._fields_ = [
    ('nr', c_int),
    ('nboundeddim', c_int),
    ('npbcdim', c_int),
    ('ncg_ideal', c_int),
    ('n', ivec),
    ('ncells', c_int),
    ('cells_nalloc', c_int),
    ('ncpddc', ivec),
    ('cell_size', rvec),
    ('cell_offset', rvec),
    ('cell_index', POINTER(c_int)),
    ('index', POINTER(c_int)),
    ('nra', POINTER(c_int)),
    ('icg0', c_int),
    ('icg1', c_int),
    ('os0', POINTER(rvec)),
    ('os1', POINTER(rvec)),
    ('a', POINTER(c_int)),
    ('nr_alloc', c_int),
    ('dcx2', POINTER(real)),
    ('dcy2', POINTER(real)),
    ('dcz2', POINTER(real)),
    ('dc_nalloc', c_int),
]

t_grid = struct_anon_100 # /home/piton/scr/gromacs-4.5.5/include/types/nsgrid.h: 72

enum_anon_101 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

enlistATOM_ATOM = 0 # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

enlistSPC_ATOM = (enlistATOM_ATOM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

enlistSPC_SPC = (enlistSPC_ATOM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

enlistTIP4P_ATOM = (enlistSPC_SPC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

enlistTIP4P_TIP4P = (enlistTIP4P_ATOM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

enlistCG_CG = (enlistTIP4P_TIP4P + 1) # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

enlistNR = (enlistCG_CG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 43

t_excl = c_ulong # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 51

# /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 85
class struct_anon_102(Structure):
    pass

struct_anon_102.__slots__ = [
    'enlist',
    'il_code',
    'icoul',
    'ivdw',
    'free_energy',
    'nri',
    'maxnri',
    'nrj',
    'maxnrj',
    'maxlen',
    'iinr',
    'iinr_end',
    'gid',
    'shift',
    'jindex',
    'jjnr',
    'jjnr_end',
    'excl',
    'count',
    'mtx',
]
struct_anon_102._fields_ = [
    ('enlist', c_int),
    ('il_code', c_int),
    ('icoul', c_int),
    ('ivdw', c_int),
    ('free_energy', c_int),
    ('nri', c_int),
    ('maxnri', c_int),
    ('nrj', c_int),
    ('maxnrj', c_int),
    ('maxlen', c_int),
    ('iinr', POINTER(c_int)),
    ('iinr_end', POINTER(c_int)),
    ('gid', POINTER(c_int)),
    ('shift', POINTER(c_int)),
    ('jindex', POINTER(c_int)),
    ('jjnr', POINTER(c_int)),
    ('jjnr_end', POINTER(c_int)),
    ('excl', POINTER(t_excl)),
    ('count', c_int),
    ('mtx', POINTER(None)),
]

t_nblist = struct_anon_102 # /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 85

enum_anon_103 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ = 0 # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDW = (eNL_VDWQQ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ = (eNL_VDW + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ_FREE = (eNL_QQ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDW_FREE = (eNL_VDWQQ_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ_FREE = (eNL_VDW_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ_WATER = (eNL_QQ_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ_WATER = (eNL_VDWQQ_WATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ_WATERWATER = (eNL_QQ_WATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ_WATERWATER = (eNL_VDWQQ_WATERWATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_NR = (eNL_QQ_WATERWATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

# /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 54
class struct_anon_104(Structure):
    pass

struct_anon_104.__slots__ = [
    'ncg',
    'nj',
    'jcg',
]
struct_anon_104._fields_ = [
    ('ncg', c_int),
    ('nj', c_int),
    ('jcg', atom_id * 1024),
]

t_ns_buf = struct_anon_104 # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 54

# /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 75
class struct_anon_105(Structure):
    pass

struct_anon_105.__slots__ = [
    'bCGlist',
    'simple_aaj',
    'grid',
    'bexcl',
    'bHaveVdW',
    'ns_buf',
    'bExcludeAlleg',
    'nra_alloc',
    'cg_alloc',
    'nl_sr',
    'nsr',
    'nl_lr_ljc',
    'nl_lr_one',
    'nlr_ljc',
    'nlr_one',
    'nblist_initialized',
    'dump_nl',
]
struct_anon_105._fields_ = [
    ('bCGlist', gmx_bool),
    ('simple_aaj', POINTER(atom_id)),
    ('grid', POINTER(t_grid)),
    ('bexcl', POINTER(t_excl)),
    ('bHaveVdW', POINTER(gmx_bool)),
    ('ns_buf', POINTER(POINTER(t_ns_buf))),
    ('bExcludeAlleg', POINTER(gmx_bool)),
    ('nra_alloc', c_int),
    ('cg_alloc', c_int),
    ('nl_sr', POINTER(POINTER(atom_id))),
    ('nsr', POINTER(c_int)),
    ('nl_lr_ljc', POINTER(POINTER(atom_id))),
    ('nl_lr_one', POINTER(POINTER(atom_id))),
    ('nlr_ljc', POINTER(c_int)),
    ('nlr_one', POINTER(c_int)),
    ('nblist_initialized', gmx_bool),
    ('dump_nl', c_int),
]

gmx_ns_t = struct_anon_105 # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 75

# /home/piton/scr/gromacs-4.5.5/include/types/genborn.h: 48
class struct_anon_106(Structure):
    pass

struct_anon_106.__slots__ = [
    'nbonds',
    'bond',
    'length',
]
struct_anon_106._fields_ = [
    ('nbonds', c_int),
    ('bond', c_int * 10),
    ('length', real * 10),
]

genborn_bonds_t = struct_anon_106 # /home/piton/scr/gromacs-4.5.5/include/types/genborn.h: 48

# /home/piton/scr/gromacs-4.5.5/include/types/genborn.h: 50
class struct_gbtmpnbls(Structure):
    pass

gbtmpnbls_t = POINTER(struct_gbtmpnbls) # /home/piton/scr/gromacs-4.5.5/include/types/genborn.h: 50

# /home/piton/scr/gromacs-4.5.5/include/types/genborn.h: 109
class struct_anon_107(Structure):
    pass

struct_anon_107.__slots__ = [
    'nr',
    'n12',
    'n13',
    'n14',
    'nalloc',
    'gpol',
    'gpol_globalindex',
    'gpol_still_work',
    'gpol_hct_work',
    'bRad',
    'vsolv',
    'vsolv_globalindex',
    'gb_radius',
    'gb_radius_globalindex',
    'use',
    'use_globalindex',
    'es',
    'asurf',
    'dasurf',
    '_as',
    'drobc',
    'param',
    'param_globalindex',
    'log_table',
    'obc_alpha',
    'obc_beta',
    'obc_gamma',
    'gb_doffset',
    'gb_epsilon_solvent',
    'epsilon_r',
    'sa_surface_tension',
    'work',
    'buf',
    'count',
    'nblist_work',
    'nblist_work_nalloc',
]
struct_anon_107._fields_ = [
    ('nr', c_int),
    ('n12', c_int),
    ('n13', c_int),
    ('n14', c_int),
    ('nalloc', c_int),
    ('gpol', POINTER(real)),
    ('gpol_globalindex', POINTER(real)),
    ('gpol_still_work', POINTER(real)),
    ('gpol_hct_work', POINTER(real)),
    ('bRad', POINTER(real)),
    ('vsolv', POINTER(real)),
    ('vsolv_globalindex', POINTER(real)),
    ('gb_radius', POINTER(real)),
    ('gb_radius_globalindex', POINTER(real)),
    ('use', POINTER(c_int)),
    ('use_globalindex', POINTER(c_int)),
    ('es', real),
    ('asurf', POINTER(real)),
    ('dasurf', POINTER(rvec)),
    ('_as', real),
    ('drobc', POINTER(real)),
    ('param', POINTER(real)),
    ('param_globalindex', POINTER(real)),
    ('log_table', POINTER(real)),
    ('obc_alpha', real),
    ('obc_beta', real),
    ('obc_gamma', real),
    ('gb_doffset', real),
    ('gb_epsilon_solvent', real),
    ('epsilon_r', real),
    ('sa_surface_tension', real),
    ('work', POINTER(real)),
    ('buf', POINTER(real)),
    ('count', POINTER(c_int)),
    ('nblist_work', gbtmpnbls_t),
    ('nblist_work_nalloc', c_int),
]

gmx_genborn_t = struct_anon_107 # /home/piton/scr/gromacs-4.5.5/include/types/genborn.h: 109

# /home/piton/scr/gromacs-4.5.5/include/types/qmmmrec.h: 83
class struct_anon_108(Structure):
    pass

struct_anon_108.__slots__ = [
    'nrQMatoms',
    'xQM',
    'indexQM',
    'atomicnumberQM',
    'QMcharges',
    'shiftQM',
    'QMcharge',
    'multiplicity',
    'QMmethod',
    'QMbasis',
    'nelectrons',
    'bTS',
    'bOPT',
    'frontatoms',
    'nQMcpus',
    'QMmem',
    'accuracy',
    'cpmcscf',
    'gauss_dir',
    'gauss_exe',
    'devel_dir',
    'orca_basename',
    'orca_dir',
    'c6',
    'c12',
    'bSH',
    'SAon',
    'SAoff',
    'SAsteps',
    'SAstep',
    'CIdim',
    'CIvec1',
    'CIvec2',
    'CIvec1old',
    'CIvec2old',
    'SHbasis',
    'CASelectrons',
    'CASorbitals',
]
struct_anon_108._fields_ = [
    ('nrQMatoms', c_int),
    ('xQM', POINTER(rvec)),
    ('indexQM', POINTER(c_int)),
    ('atomicnumberQM', POINTER(c_int)),
    ('QMcharges', POINTER(real)),
    ('shiftQM', POINTER(c_int)),
    ('QMcharge', c_int),
    ('multiplicity', c_int),
    ('QMmethod', c_int),
    ('QMbasis', c_int),
    ('nelectrons', c_int),
    ('bTS', gmx_bool),
    ('bOPT', gmx_bool),
    ('frontatoms', POINTER(gmx_bool)),
    ('nQMcpus', c_int),
    ('QMmem', c_int),
    ('accuracy', c_int),
    ('cpmcscf', gmx_bool),
    ('gauss_dir', String),
    ('gauss_exe', String),
    ('devel_dir', String),
    ('orca_basename', String),
    ('orca_dir', String),
    ('c6', POINTER(real)),
    ('c12', POINTER(real)),
    ('bSH', gmx_bool),
    ('SAon', real),
    ('SAoff', real),
    ('SAsteps', c_int),
    ('SAstep', c_int),
    ('CIdim', c_int),
    ('CIvec1', POINTER(real)),
    ('CIvec2', POINTER(real)),
    ('CIvec1old', POINTER(real)),
    ('CIvec2old', POINTER(real)),
    ('SHbasis', ivec),
    ('CASelectrons', c_int),
    ('CASorbitals', c_int),
]

t_QMrec = struct_anon_108 # /home/piton/scr/gromacs-4.5.5/include/types/qmmmrec.h: 83

# /home/piton/scr/gromacs-4.5.5/include/types/qmmmrec.h: 96
class struct_anon_109(Structure):
    pass

struct_anon_109.__slots__ = [
    'nrMMatoms',
    'xMM',
    'indexMM',
    'MMcharges',
    'shiftMM',
    'MMatomtype',
    'scalefactor',
    'c6',
    'c12',
]
struct_anon_109._fields_ = [
    ('nrMMatoms', c_int),
    ('xMM', POINTER(rvec)),
    ('indexMM', POINTER(c_int)),
    ('MMcharges', POINTER(real)),
    ('shiftMM', POINTER(c_int)),
    ('MMatomtype', POINTER(c_int)),
    ('scalefactor', real),
    ('c6', POINTER(real)),
    ('c12', POINTER(real)),
]

t_MMrec = struct_anon_109 # /home/piton/scr/gromacs-4.5.5/include/types/qmmmrec.h: 96

# /home/piton/scr/gromacs-4.5.5/include/types/qmmmrec.h: 104
class struct_anon_110(Structure):
    pass

struct_anon_110.__slots__ = [
    'QMMMscheme',
    'nrQMlayers',
    'qm',
    'mm',
]
struct_anon_110._fields_ = [
    ('QMMMscheme', c_int),
    ('nrQMlayers', c_int),
    ('qm', POINTER(POINTER(t_QMrec))),
    ('mm', POINTER(t_MMrec)),
]

t_QMMMrec = struct_anon_110 # /home/piton/scr/gromacs-4.5.5/include/types/qmmmrec.h: 104

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 46
class struct_gmx_pme(Structure):
    pass

gmx_pme_t = POINTER(struct_gmx_pme) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 46

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 56
class struct_anon_111(Structure):
    pass

struct_anon_111.__slots__ = [
    'r',
    'n',
    'scale',
    'scale_exp',
    'tab',
]
struct_anon_111._fields_ = [
    ('r', real),
    ('n', c_int),
    ('scale', real),
    ('scale_exp', real),
    ('tab', POINTER(real)),
]

t_forcetable = struct_anon_111 # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 56

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 68
class struct_anon_112(Structure):
    pass

struct_anon_112.__slots__ = [
    'tab',
    'coultab',
    'vdwtab',
    'nlist_sr',
    'nlist_lr',
]
struct_anon_112._fields_ = [
    ('tab', t_forcetable),
    ('coultab', POINTER(real)),
    ('vdwtab', POINTER(real)),
    ('nlist_sr', t_nblist * eNL_NR),
    ('nlist_lr', t_nblist * eNL_NR),
]

t_nblists = struct_anon_112 # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 68

enum_anon_113 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egCOULSR = 0 # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egLJSR = (egCOULSR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egBHAMSR = (egLJSR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egCOULLR = (egBHAMSR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egLJLR = (egCOULLR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egBHAMLR = (egLJLR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egCOUL14 = (egBHAMLR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egLJ14 = (egCOUL14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egGB = (egLJ14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

egNR = (egGB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 99

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 105
class struct_anon_114(Structure):
    pass

struct_anon_114.__slots__ = [
    'nener',
    'ener',
]
struct_anon_114._fields_ = [
    ('nener', c_int),
    ('ener', POINTER(real) * egNR),
]

gmx_grppairener_t = struct_anon_114 # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 105

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 114
class struct_anon_115(Structure):
    pass

struct_anon_115.__slots__ = [
    'term',
    'grpp',
    'dvdl_lin',
    'dvdl_nonlin',
    'n_lambda',
    'enerpart_lambda',
]
struct_anon_115._fields_ = [
    ('term', real * F_NRE),
    ('grpp', gmx_grppairener_t),
    ('dvdl_lin', c_double),
    ('dvdl_nonlin', c_double),
    ('n_lambda', c_int),
    ('enerpart_lambda', POINTER(c_double)),
]

gmx_enerdata_t = struct_anon_115 # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 114

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 126
class struct_anon_116(Structure):
    pass

struct_anon_116.__slots__ = [
    'cg_start',
    'cg_end',
    'cg_mod',
    'cginfo',
]
struct_anon_116._fields_ = [
    ('cg_start', c_int),
    ('cg_end', c_int),
    ('cg_mod', c_int),
    ('cginfo', POINTER(c_int)),
]

cginfo_mb_t = struct_anon_116 # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 126

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 130
class struct_ewald_tab(Structure):
    pass

ewald_tab_t = POINTER(struct_ewald_tab) # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 130

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 369
class struct_anon_117(Structure):
    pass

struct_anon_117.__slots__ = [
    'bDomDec',
    'ePBC',
    'bMolPBC',
    'rc_scaling',
    'posres_com',
    'posres_comB',
    'UseOptimizedKernels',
    'bAllvsAll',
    'AllvsAll_work',
    'AllvsAll_workgb',
    'rlist',
    'rlistlong',
    'zsquare',
    'temp',
    'epsilon_r',
    'epsilon_rf',
    'epsfac',
    'kappa',
    'k_rf',
    'c_rf',
    'qsum',
    'mu_tot',
    'eDispCorr',
    'enershiftsix',
    'enershifttwelve',
    'enerdiffsix',
    'enerdifftwelve',
    'virdiffsix',
    'virdifftwelve',
    'avcsix',
    'avctwelve',
    'fudgeQQ',
    'bcoultab',
    'bvdwtab',
    'tab14',
    'rcoulomb_switch',
    'rcoulomb',
    'phi',
    'reppow',
    'rvdw_switch',
    'rvdw',
    'bham_b_max',
    'efep',
    'sc_alpha',
    'sc_power',
    'sc_sigma6_def',
    'sc_sigma6_min',
    'bSepDVDL',
    'eeltype',
    'vdwtype',
    'cg0',
    'hcg',
    'solvent_opt',
    'nWatMol',
    'bGrid',
    'cginfo_mb',
    'cginfo',
    'cg_cm',
    'cg_nalloc',
    'shift_vec',
    'nnblists',
    'gid2nblists',
    'nblists',
    'nwall',
    'wall_tab',
    'ncg_force',
    'natoms_force',
    'natoms_force_constr',
    'nalloc_force',
    'bTwinRange',
    'nlr',
    'f_twin',
    'bF_NoVirSum',
    'f_novirsum_n',
    'f_novirsum_nalloc',
    'f_novirsum_alloc',
    'f_novirsum',
    'pmedata',
    'vir_el_recip',
    'bEwald',
    'ewaldcoeff',
    'ewald_table',
    'fshift',
    'vir_diag_posres',
    'vir_wall_z',
    'ntype',
    'bBHAM',
    'nbfp',
    'egp_flags',
    'fc_stepsize',
    'bGB',
    'gb_epsilon_solvent',
    'gbtab',
    'atype_radius',
    'atype_vol',
    'atype_surftens',
    'atype_gb_radius',
    'atype_S_hct',
    'born',
    'gbtabscale',
    'gbtabr',
    'gblist_sr',
    'gblist_lr',
    'gblist',
    'invsqrta',
    'dvda',
    'dadx',
    'dadx_rawptr',
    'nalloc_dadx',
    'n_tpi',
    'ns',
    'bQMMM',
    'qr',
    'QMMMlist',
    'print_force',
    't_fnbf',
    't_wait',
    'timesteps',
    'userint1',
    'userint2',
    'userint3',
    'userint4',
    'userreal1',
    'userreal2',
    'userreal3',
    'userreal4',
]
struct_anon_117._fields_ = [
    ('bDomDec', gmx_bool),
    ('ePBC', c_int),
    ('bMolPBC', gmx_bool),
    ('rc_scaling', c_int),
    ('posres_com', rvec),
    ('posres_comB', rvec),
    ('UseOptimizedKernels', gmx_bool),
    ('bAllvsAll', gmx_bool),
    ('AllvsAll_work', POINTER(None)),
    ('AllvsAll_workgb', POINTER(None)),
    ('rlist', real),
    ('rlistlong', real),
    ('zsquare', real),
    ('temp', real),
    ('epsilon_r', real),
    ('epsilon_rf', real),
    ('epsfac', real),
    ('kappa', real),
    ('k_rf', real),
    ('c_rf', real),
    ('qsum', c_double * 2),
    ('mu_tot', rvec * 2),
    ('eDispCorr', c_int),
    ('enershiftsix', real),
    ('enershifttwelve', real),
    ('enerdiffsix', real),
    ('enerdifftwelve', real),
    ('virdiffsix', real),
    ('virdifftwelve', real),
    ('avcsix', real * 2),
    ('avctwelve', real * 2),
    ('fudgeQQ', real),
    ('bcoultab', gmx_bool),
    ('bvdwtab', gmx_bool),
    ('tab14', t_forcetable),
    ('rcoulomb_switch', real),
    ('rcoulomb', real),
    ('phi', POINTER(real)),
    ('reppow', c_double),
    ('rvdw_switch', real),
    ('rvdw', real),
    ('bham_b_max', real),
    ('efep', c_int),
    ('sc_alpha', real),
    ('sc_power', c_int),
    ('sc_sigma6_def', real),
    ('sc_sigma6_min', real),
    ('bSepDVDL', gmx_bool),
    ('eeltype', c_int),
    ('vdwtype', c_int),
    ('cg0', c_int),
    ('hcg', c_int),
    ('solvent_opt', c_int),
    ('nWatMol', c_int),
    ('bGrid', gmx_bool),
    ('cginfo_mb', POINTER(cginfo_mb_t)),
    ('cginfo', POINTER(c_int)),
    ('cg_cm', POINTER(rvec)),
    ('cg_nalloc', c_int),
    ('shift_vec', POINTER(rvec)),
    ('nnblists', c_int),
    ('gid2nblists', POINTER(c_int)),
    ('nblists', POINTER(t_nblists)),
    ('nwall', c_int),
    ('wall_tab', POINTER(POINTER(t_forcetable))),
    ('ncg_force', c_int),
    ('natoms_force', c_int),
    ('natoms_force_constr', c_int),
    ('nalloc_force', c_int),
    ('bTwinRange', gmx_bool),
    ('nlr', c_int),
    ('f_twin', POINTER(rvec)),
    ('bF_NoVirSum', gmx_bool),
    ('f_novirsum_n', c_int),
    ('f_novirsum_nalloc', c_int),
    ('f_novirsum_alloc', POINTER(rvec)),
    ('f_novirsum', POINTER(rvec)),
    ('pmedata', gmx_pme_t),
    ('vir_el_recip', tensor),
    ('bEwald', gmx_bool),
    ('ewaldcoeff', real),
    ('ewald_table', ewald_tab_t),
    ('fshift', POINTER(rvec)),
    ('vir_diag_posres', rvec),
    ('vir_wall_z', dvec),
    ('ntype', c_int),
    ('bBHAM', gmx_bool),
    ('nbfp', POINTER(real)),
    ('egp_flags', POINTER(c_int)),
    ('fc_stepsize', real),
    ('bGB', gmx_bool),
    ('gb_epsilon_solvent', real),
    ('gbtab', t_forcetable),
    ('atype_radius', POINTER(real)),
    ('atype_vol', POINTER(real)),
    ('atype_surftens', POINTER(real)),
    ('atype_gb_radius', POINTER(real)),
    ('atype_S_hct', POINTER(real)),
    ('born', POINTER(gmx_genborn_t)),
    ('gbtabscale', real),
    ('gbtabr', real),
    ('gblist_sr', t_nblist),
    ('gblist_lr', t_nblist),
    ('gblist', t_nblist),
    ('invsqrta', POINTER(real)),
    ('dvda', POINTER(real)),
    ('dadx', POINTER(real)),
    ('dadx_rawptr', POINTER(real)),
    ('nalloc_dadx', c_int),
    ('n_tpi', gmx_bool),
    ('ns', gmx_ns_t),
    ('bQMMM', gmx_bool),
    ('qr', POINTER(t_QMMMrec)),
    ('QMMMlist', t_nblist),
    ('print_force', real),
    ('t_fnbf', c_double),
    ('t_wait', c_double),
    ('timesteps', c_int),
    ('userint1', c_int),
    ('userint2', c_int),
    ('userint3', c_int),
    ('userint4', c_int),
    ('userreal1', real),
    ('userreal2', real),
    ('userreal3', real),
    ('userreal4', real),
]

t_forcerec = struct_anon_117 # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 369

enum_anon_118 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 52

eglsNABNSB = 0 # /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 52

eglsCHKPT = (eglsNABNSB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 52

eglsSTOPCOND = (eglsCHKPT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 52

eglsRESETCOUNTERS = (eglsSTOPCOND + 1) # /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 52

eglsNR = (eglsRESETCOUNTERS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 52

# /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 58
class struct_anon_119(Structure):
    pass

struct_anon_119.__slots__ = [
    'nstms',
    'sig',
    'set',
]
struct_anon_119._fields_ = [
    ('nstms', c_int),
    ('sig', c_int * eglsNR),
    ('set', c_int * eglsNR),
]

globsig_t = struct_anon_119 # /home/piton/scr/gromacs-4.5.5/include/types/globsig.h: 58

enum_anon_120 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 43

egcolWhite = 0 # /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 43

egcolGrey = (egcolWhite + 1) # /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 43

egcolBlack = (egcolGrey + 1) # /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 43

egcolNR = (egcolBlack + 1) # /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 43

egCol = enum_anon_120 # /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 43

# /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 56
class struct_anon_121(Structure):
    pass

struct_anon_121.__slots__ = [
    'nnodes',
    'nbound',
    'start',
    'end',
    'nedge',
    'edge',
    'bScrewPBC',
    'ishift',
    'negc',
    'egc',
]
struct_anon_121._fields_ = [
    ('nnodes', c_int),
    ('nbound', c_int),
    ('start', c_int),
    ('end', c_int),
    ('nedge', POINTER(c_int)),
    ('edge', POINTER(POINTER(atom_id))),
    ('bScrewPBC', gmx_bool),
    ('ishift', POINTER(ivec)),
    ('negc', c_int),
    ('egc', POINTER(egCol)),
]

t_graph = struct_anon_121 # /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 56

# /home/piton/scr/gromacs-4.5.5/include/types/group.h: 54
class struct_anon_122(Structure):
    pass

struct_anon_122.__slots__ = [
    'Th',
    'T',
    'ekinh',
    'ekinh_old',
    'ekinf',
    '_lambda',
    'ekinscalef_nhc',
    'ekinscaleh_nhc',
    'vscale_nhc',
]
struct_anon_122._fields_ = [
    ('Th', real),
    ('T', real),
    ('ekinh', tensor),
    ('ekinh_old', tensor),
    ('ekinf', tensor),
    ('_lambda', real),
    ('ekinscalef_nhc', c_double),
    ('ekinscaleh_nhc', c_double),
    ('vscale_nhc', c_double),
]

t_grp_tcstat = struct_anon_122 # /home/piton/scr/gromacs-4.5.5/include/types/group.h: 54

# /home/piton/scr/gromacs-4.5.5/include/types/group.h: 62
class struct_anon_123(Structure):
    pass

struct_anon_123.__slots__ = [
    'nat',
    'u',
    'uold',
    'mA',
    'mB',
]
struct_anon_123._fields_ = [
    ('nat', c_int),
    ('u', rvec),
    ('uold', rvec),
    ('mA', c_double),
    ('mB', c_double),
]

t_grp_acc = struct_anon_123 # /home/piton/scr/gromacs-4.5.5/include/types/group.h: 62

# /home/piton/scr/gromacs-4.5.5/include/types/group.h: 68
class struct_anon_124(Structure):
    pass

struct_anon_124.__slots__ = [
    'cos_accel',
    'mvcos',
    'vcos',
]
struct_anon_124._fields_ = [
    ('cos_accel', real),
    ('mvcos', real),
    ('vcos', real),
]

t_cos_acc = struct_anon_124 # /home/piton/scr/gromacs-4.5.5/include/types/group.h: 68

# /home/piton/scr/gromacs-4.5.5/include/types/group.h: 81
class struct_anon_125(Structure):
    pass

struct_anon_125.__slots__ = [
    'bNEMD',
    'ngtc',
    'tcstat',
    'ngacc',
    'grpstat',
    'ekin',
    'ekinh',
    'dekindl',
    'dekindl_old',
    'cosacc',
]
struct_anon_125._fields_ = [
    ('bNEMD', gmx_bool),
    ('ngtc', c_int),
    ('tcstat', POINTER(t_grp_tcstat)),
    ('ngacc', c_int),
    ('grpstat', POINTER(t_grp_acc)),
    ('ekin', tensor),
    ('ekinh', tensor),
    ('dekindl', real),
    ('dekindl_old', real),
    ('cosacc', t_cos_acc),
]

gmx_ekindata_t = struct_anon_125 # /home/piton/scr/gromacs-4.5.5/include/types/group.h: 81

__off_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 141

__off64_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 142

# /usr/include/libio.h: 271
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE # /usr/include/stdio.h: 49

_IO_lock_t = None # /usr/include/libio.h: 180

# /usr/include/libio.h: 186
class struct__IO_marker(Structure):
    pass

struct__IO_marker.__slots__ = [
    '_next',
    '_sbuf',
    '_pos',
]
struct__IO_marker._fields_ = [
    ('_next', POINTER(struct__IO_marker)),
    ('_sbuf', POINTER(struct__IO_FILE)),
    ('_pos', c_int),
]

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '__pad1',
    '__pad2',
    '__pad3',
    '__pad4',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', POINTER(None)),
    ('__pad2', POINTER(None)),
    ('__pad3', POINTER(None)),
    ('__pad4', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
]

enum_anon_173 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 42

epbcXYZ = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 42

epbcNONE = (epbcXYZ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 42

epbcXY = (epbcNONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 42

epbcSCREW = (epbcXY + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 42

epbcNR = (epbcSCREW + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 42

enum_anon_174 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcBERENDSEN = (etcNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcNOSEHOOVER = (etcBERENDSEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcYES = (etcNOSEHOOVER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcANDERSEN = (etcYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcANDERSENINTERVAL = (etcANDERSEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcVRESCALE = (etcANDERSENINTERVAL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

etcNR = (etcVRESCALE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 46

enum_anon_175 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 50

epcNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 50

epcBERENDSEN = (epcNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 50

epcPARRINELLORAHMAN = (epcBERENDSEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 50

epcISOTROPIC = (epcPARRINELLORAHMAN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 50

epcMTTK = (epcISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 50

epcNR = (epcMTTK + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 50

enum_anon_176 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtNONE = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtNHC = (etrtNONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtBAROV = (etrtNHC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtBARONHC = (etrtBAROV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtNHC2 = (etrtBARONHC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtBAROV2 = (etrtNHC2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtBARONHC2 = (etrtBAROV2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtVELOCITY1 = (etrtBARONHC2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtVELOCITY2 = (etrtVELOCITY1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtPOSITION = (etrtVELOCITY2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtSKIPALL = (etrtPOSITION + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

etrtNR = (etrtSKIPALL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 55

enum_anon_177 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 61

ettTSEQ0 = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 61

ettTSEQ1 = (ettTSEQ0 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 61

ettTSEQ2 = (ettTSEQ1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 61

ettTSEQ3 = (ettTSEQ2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 61

ettTSEQ4 = (ettTSEQ3 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 61

ettTSEQMAX = (ettTSEQ4 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 61

enum_anon_178 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 65

epctISOTROPIC = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 65

epctSEMIISOTROPIC = (epctISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 65

epctANISOTROPIC = (epctSEMIISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 65

epctSURFACETENSION = (epctANISOTROPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 65

epctNR = (epctSURFACETENSION + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 65

enum_anon_179 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 70

erscNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 70

erscALL = (erscNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 70

erscCOM = (erscALL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 70

erscNR = (erscCOM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 70

enum_anon_180 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelCUT = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelRF = (eelCUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelGRF = (eelRF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelPME = (eelGRF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelEWALD = (eelPME + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelPPPM = (eelEWALD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelPOISSON = (eelPPPM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelSWITCH = (eelPOISSON + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelSHIFT = (eelSWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelUSER = (eelSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelGB_NOTUSED = (eelUSER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelRF_NEC = (eelGB_NOTUSED + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelENCADSHIFT = (eelRF_NEC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelPMEUSER = (eelENCADSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelPMESWITCH = (eelPMEUSER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelPMEUSERSWITCH = (eelPMESWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelRF_ZERO = (eelPMEUSERSWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

eelNR = (eelRF_ZERO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 79

enum_anon_181 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 86

eewg3D = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 86

eewg3DC = (eewg3D + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 86

eewgNR = (eewg3DC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 86

enum_anon_182 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 101

evdwCUT = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 101

evdwSWITCH = (evdwCUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 101

evdwSHIFT = (evdwSWITCH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 101

evdwUSER = (evdwSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 101

evdwENCADSHIFT = (evdwUSER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 101

evdwNR = (evdwENCADSHIFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 101

enum_anon_183 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 111

ensGRID = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 111

ensSIMPLE = (ensGRID + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 111

ensNR = (ensSIMPLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 111

enum_anon_184 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiMD = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiSteep = (eiMD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiCG = (eiSteep + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiBD = (eiCG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiSD2 = (eiBD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiNM = (eiSD2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiLBFGS = (eiNM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiTPI = (eiLBFGS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiTPIC = (eiTPI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiSD1 = (eiTPIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiVV = (eiSD1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiVVAK = (eiVV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

eiNR = (eiVVAK + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 118

enum_anon_185 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 131

econtLINCS = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 131

econtSHAKE = (econtLINCS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 131

econtNR = (econtSHAKE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 131

enum_anon_186 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 135

edrNone = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 135

edrSimple = (edrNone + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 135

edrEnsemble = (edrSimple + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 135

edrNR = (edrEnsemble + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 135

enum_anon_187 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 139

edrwConservative = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 139

edrwEqual = (edrwConservative + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 139

edrwNR = (edrwEqual + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 139

enum_anon_188 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 144

eCOMB_NONE = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 144

eCOMB_GEOMETRIC = (eCOMB_NONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 144

eCOMB_ARITHMETIC = (eCOMB_GEOMETRIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 144

eCOMB_GEOM_SIG_EPS = (eCOMB_ARITHMETIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 144

eCOMB_NR = (eCOMB_GEOM_SIG_EPS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 144

enum_anon_189 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 149

eNBF_NONE = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 149

eNBF_LJ = (eNBF_NONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 149

eNBF_BHAM = (eNBF_LJ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 149

eNBF_NR = (eNBF_BHAM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 149

enum_anon_190 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 154

efepNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 154

efepYES = (efepNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 154

efepNR = (efepYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 154

enum_anon_191 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 159

sepdhdlfileYES = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 159

sepdhdlfileNO = (sepdhdlfileYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 159

sepdhdlfileNR = (sepdhdlfileNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 159

enum_anon_192 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 166

dhdlderivativesYES = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 166

dhdlderivativesNO = (dhdlderivativesYES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 166

dhdlderivativesNR = (dhdlderivativesNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 166

enum_anon_193 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 173

esolNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 173

esolSPC = (esolNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 173

esolTIP4P = (esolSPC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 173

esolNR = (esolTIP4P + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 173

enum_anon_194 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 178

edispcNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 178

edispcEnerPres = (edispcNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 178

edispcEner = (edispcEnerPres + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 178

edispcAllEnerPres = (edispcEner + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 178

edispcAllEner = (edispcAllEnerPres + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 178

edispcNR = (edispcAllEner + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 178

enum_anon_195 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 183

eshellCSH = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 183

eshellBASH = (eshellCSH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 183

eshellZSH = (eshellBASH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 183

eshellNR = (eshellZSH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 183

enum_anon_196 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 188

ecmLINEAR = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 188

ecmANGULAR = (ecmLINEAR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 188

ecmNO = (ecmANGULAR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 188

ecmNR = (ecmNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 188

enum_anon_197 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 193

eannNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 193

eannSINGLE = (eannNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 193

eannPERIODIC = (eannSINGLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 193

eannNR = (eannPERIODIC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 193

enum_anon_198 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 198

eisNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 198

eisGBSA = (eisNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 198

eisNR = (eisGBSA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 198

enum_anon_199 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 203

egbSTILL = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 203

egbHCT = (egbSTILL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 203

egbOBC = (egbHCT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 203

egbNR = (egbOBC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 203

enum_anon_200 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 207

esaAPPROX = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 207

esaNO = (esaAPPROX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 207

esaSTILL = (esaNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 207

esaNR = (esaSTILL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 207

enum_anon_201 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 212

ewt93 = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 212

ewt104 = (ewt93 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 212

ewtTABLE = (ewt104 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 212

ewt126 = (ewtTABLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 212

ewtNR = (ewt126 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 212

enum_anon_202 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 217

epullNO = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 217

epullUMBRELLA = (epullNO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 217

epullCONSTRAINT = (epullUMBRELLA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 217

epullCONST_F = (epullCONSTRAINT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 217

epullNR = (epullCONST_F + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 217

enum_anon_203 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 221

epullgDIST = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 221

epullgDIR = (epullgDIST + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 221

epullgCYL = (epullgDIR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 221

epullgPOS = (epullgCYL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 221

epullgDIRPBC = (epullgPOS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 221

epullgNR = (epullgDIRPBC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 221

enum_anon_204 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodAM1 = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodPM3 = (eQMmethodAM1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodRHF = (eQMmethodPM3 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodUHF = (eQMmethodRHF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodDFT = (eQMmethodUHF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodB3LYP = (eQMmethodDFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodMP2 = (eQMmethodB3LYP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodCASSCF = (eQMmethodMP2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodB3LYPLAN = (eQMmethodCASSCF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodDIRECT = (eQMmethodB3LYPLAN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

eQMmethodNR = (eQMmethodDIRECT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 228

enum_anon_205 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasisSTO3G = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasisSTO3G2 = (eQMbasisSTO3G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis321G = (eQMbasisSTO3G2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis321Gp = (eQMbasis321G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis321dGp = (eQMbasis321Gp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis621G = (eQMbasis321dGp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis631G = (eQMbasis621G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis631Gp = (eQMbasis631G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis631dGp = (eQMbasis631Gp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasis6311G = (eQMbasis631dGp + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

eQMbasisNR = (eQMbasis6311G + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 234

enum_anon_206 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 241

eQMMMschemenormal = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 241

eQMMMschemeoniom = (eQMMMschemenormal + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 241

eQMMMschemeNR = (eQMMMschemeoniom + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 241

enum_anon_207 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 245

eMultentOptName = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 245

eMultentOptNo = (eMultentOptName + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 245

eMultentOptLast = (eMultentOptNo + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 245

eMultentOptNR = (eMultentOptLast + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 245

# /home/piton/scr/gromacs-4.5.5/include/types/../types/symtab.h: 43
class struct_symbuf(Structure):
    pass

struct_symbuf.__slots__ = [
    'bufsize',
    'buf',
    'next',
]
struct_symbuf._fields_ = [
    ('bufsize', c_int),
    ('buf', POINTER(POINTER(c_char))),
    ('next', POINTER(struct_symbuf)),
]

t_symbuf = struct_symbuf # /home/piton/scr/gromacs-4.5.5/include/types/../types/symtab.h: 47

# /home/piton/scr/gromacs-4.5.5/include/types/../types/symtab.h: 53
class struct_anon_208(Structure):
    pass

struct_anon_208.__slots__ = [
    'nr',
    'symbuf',
]
struct_anon_208._fields_ = [
    ('nr', c_int),
    ('symbuf', POINTER(t_symbuf)),
]

t_symtab = struct_anon_208 # /home/piton/scr/gromacs-4.5.5/include/types/../types/symtab.h: 53

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 123
class struct_anon_210(Structure):
    pass

struct_anon_210.__slots__ = [
    'database',
    'accession',
    'date',
    'title',
    'remarklen',
    'remarks',
]
struct_anon_210._fields_ = [
    ('database', c_char * 81),
    ('accession', c_char * 81),
    ('date', c_char * 81),
    ('title', c_char * 81),
    ('remarklen', c_int),
    ('remarks', String),
]

molfile_metadata_t = struct_anon_210 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 123

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 159
class struct_anon_211(Structure):
    pass

struct_anon_211.__slots__ = [
    'name',
    'type',
    'resname',
    'resid',
    'segid',
    'chain',
    'altloc',
    'insertion',
    'occupancy',
    'bfactor',
    'mass',
    'charge',
    'radius',
    'atomicnumber',
]
struct_anon_211._fields_ = [
    ('name', c_char * 16),
    ('type', c_char * 16),
    ('resname', c_char * 8),
    ('resid', c_int),
    ('segid', c_char * 8),
    ('chain', c_char * 2),
    ('altloc', c_char * 2),
    ('insertion', c_char * 2),
    ('occupancy', c_float),
    ('bfactor', c_float),
    ('mass', c_float),
    ('charge', c_float),
    ('radius', c_float),
    ('atomicnumber', c_int),
]

molfile_atom_t = struct_anon_211 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 159

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 189
class struct_molfile_timestep_metadata(Structure):
    pass

struct_molfile_timestep_metadata.__slots__ = [
    'count',
    'avg_bytes_per_timestep',
    'has_velocities',
]
struct_molfile_timestep_metadata._fields_ = [
    ('count', c_uint),
    ('avg_bytes_per_timestep', c_uint),
    ('has_velocities', c_int),
]

molfile_timestep_metadata_t = struct_molfile_timestep_metadata # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 189

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 205
class struct_molfile_qm_timestep_metadata(Structure):
    pass

struct_molfile_qm_timestep_metadata.__slots__ = [
    'count',
    'avg_bytes_per_timestep',
    'has_gradient',
    'num_scfiter',
    'num_orbitals_per_wavef',
    'has_orben_per_wavef',
    'has_occup_per_wavef',
    'num_wavef',
    'wavef_size',
    'num_charge_sets',
]
struct_molfile_qm_timestep_metadata._fields_ = [
    ('count', c_uint),
    ('avg_bytes_per_timestep', c_uint),
    ('has_gradient', c_int),
    ('num_scfiter', c_int),
    ('num_orbitals_per_wavef', c_int * 25),
    ('has_orben_per_wavef', c_int * 25),
    ('has_occup_per_wavef', c_int * 25),
    ('num_wavef', c_int),
    ('wavef_size', c_int),
    ('num_charge_sets', c_int),
]

molfile_qm_timestep_metadata_t = struct_molfile_qm_timestep_metadata # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 205

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 232
class struct_anon_212(Structure):
    pass

struct_anon_212.__slots__ = [
    'coords',
    'velocities',
    'A',
    'B',
    'C',
    'alpha',
    'beta',
    'gamma',
    'physical_time',
]
struct_anon_212._fields_ = [
    ('coords', POINTER(c_float)),
    ('velocities', POINTER(c_float)),
    ('A', c_float),
    ('B', c_float),
    ('C', c_float),
    ('alpha', c_float),
    ('beta', c_float),
    ('gamma', c_float),
    ('physical_time', c_double),
]

molfile_timestep_t = struct_anon_212 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 232

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 267
class struct_anon_213(Structure):
    pass

struct_anon_213.__slots__ = [
    'dataname',
    'origin',
    'xaxis',
    'yaxis',
    'zaxis',
    'xsize',
    'ysize',
    'zsize',
    'has_color',
]
struct_anon_213._fields_ = [
    ('dataname', c_char * 256),
    ('origin', c_float * 3),
    ('xaxis', c_float * 3),
    ('yaxis', c_float * 3),
    ('zaxis', c_float * 3),
    ('xsize', c_int),
    ('ysize', c_int),
    ('zsize', c_int),
    ('has_color', c_int),
]

molfile_volumetric_t = struct_anon_213 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 267

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 296
class struct_anon_214(Structure):
    pass

struct_anon_214.__slots__ = [
    'nimag',
    'nintcoords',
    'ncart',
    'num_basis_funcs',
    'num_basis_atoms',
    'num_shells',
    'wavef_size',
    'have_sysinfo',
    'have_carthessian',
    'have_inthessian',
    'have_normalmodes',
]
struct_anon_214._fields_ = [
    ('nimag', c_int),
    ('nintcoords', c_int),
    ('ncart', c_int),
    ('num_basis_funcs', c_int),
    ('num_basis_atoms', c_int),
    ('num_shells', c_int),
    ('wavef_size', c_int),
    ('have_sysinfo', c_int),
    ('have_carthessian', c_int),
    ('have_inthessian', c_int),
    ('have_normalmodes', c_int),
]

molfile_qm_metadata_t = struct_anon_214 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 296

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 314
class struct_anon_215(Structure):
    pass

struct_anon_215.__slots__ = [
    'carthessian',
    'imag_modes',
    'inthessian',
    'wavenumbers',
    'intensities',
    'normalmodes',
]
struct_anon_215._fields_ = [
    ('carthessian', POINTER(c_double)),
    ('imag_modes', POINTER(c_int)),
    ('inthessian', POINTER(c_double)),
    ('wavenumbers', POINTER(c_float)),
    ('intensities', POINTER(c_float)),
    ('normalmodes', POINTER(c_float)),
]

molfile_qm_hessian_t = struct_anon_215 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 314

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 335
class struct_anon_216(Structure):
    pass

struct_anon_216.__slots__ = [
    'num_shells_per_atom',
    'num_prim_per_shell',
    'basis',
    'atomic_number',
    'angular_momentum',
    'shell_symmetry',
]
struct_anon_216._fields_ = [
    ('num_shells_per_atom', POINTER(c_int)),
    ('num_prim_per_shell', POINTER(c_int)),
    ('basis', POINTER(c_float)),
    ('atomic_number', POINTER(c_int)),
    ('angular_momentum', POINTER(c_int)),
    ('shell_symmetry', POINTER(c_int)),
]

molfile_qm_basis_t = struct_anon_216 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 335

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 360
class struct_anon_217(Structure):
    pass

struct_anon_217.__slots__ = [
    'nproc',
    'memory',
    'runtype',
    'scftype',
    'status',
    'num_electrons',
    'totalcharge',
    'num_occupied_A',
    'num_occupied_B',
    'nuc_charge',
    'basis_string',
    'runtitle',
    'geometry',
    'version_string',
]
struct_anon_217._fields_ = [
    ('nproc', c_int),
    ('memory', c_int),
    ('runtype', c_int),
    ('scftype', c_int),
    ('status', c_int),
    ('num_electrons', c_int),
    ('totalcharge', c_int),
    ('num_occupied_A', c_int),
    ('num_occupied_B', c_int),
    ('nuc_charge', POINTER(c_double)),
    ('basis_string', c_char * 81),
    ('runtitle', c_char * 4096),
    ('geometry', c_char * 81),
    ('version_string', c_char * 81),
]

molfile_qm_sysinfo_t = struct_anon_217 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 360

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 380
class struct_anon_218(Structure):
    pass

struct_anon_218.__slots__ = [
    'type',
    'spin',
    'excitation',
    'multiplicity',
    'info',
    'energy',
    'wave_coeffs',
    'orbital_energies',
    'occupancies',
    'orbital_ids',
]
struct_anon_218._fields_ = [
    ('type', c_int),
    ('spin', c_int),
    ('excitation', c_int),
    ('multiplicity', c_int),
    ('info', c_char * 81),
    ('energy', c_double),
    ('wave_coeffs', POINTER(c_float)),
    ('orbital_energies', POINTER(c_float)),
    ('occupancies', POINTER(c_float)),
    ('orbital_ids', POINTER(c_int)),
]

molfile_qm_wavefunction_t = struct_anon_218 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 380

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 393
class struct_anon_219(Structure):
    pass

struct_anon_219.__slots__ = [
    'wave',
    'gradient',
    'scfenergies',
    'charges',
    'charge_types',
]
struct_anon_219._fields_ = [
    ('wave', POINTER(molfile_qm_wavefunction_t)),
    ('gradient', POINTER(c_float)),
    ('scfenergies', POINTER(c_double)),
    ('charges', POINTER(c_double)),
    ('charge_types', POINTER(c_int)),
]

molfile_qm_timestep_t = struct_anon_219 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 393

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 403
class struct_anon_220(Structure):
    pass

struct_anon_220.__slots__ = [
    'hess',
    'basis',
    'run',
]
struct_anon_220._fields_ = [
    ('hess', molfile_qm_hessian_t),
    ('basis', molfile_qm_basis_t),
    ('run', molfile_qm_sysinfo_t),
]

molfile_qm_t = struct_anon_220 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 403

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 470
class struct_anon_221(Structure):
    pass

struct_anon_221.__slots__ = [
    'type',
    'style',
    'size',
    'data',
]
struct_anon_221._fields_ = [
    ('type', c_int),
    ('style', c_int),
    ('size', c_float),
    ('data', c_float * 9),
]

molfile_graphics_t = struct_anon_221 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 470

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 810
class struct_anon_222(Structure):
    pass

struct_anon_222.__slots__ = [
    'abiversion',
    'type',
    'name',
    'prettyname',
    'author',
    'majorv',
    'minorv',
    'is_reentrant',
    'filename_extension',
    'open_file_read',
    'read_structure',
    'read_bonds',
    'read_next_timestep',
    'close_file_read',
    'open_file_write',
    'write_structure',
    'write_timestep',
    'close_file_write',
    'read_volumetric_metadata',
    'read_volumetric_data',
    'read_rawgraphics',
    'read_molecule_metadata',
    'write_bonds',
    'write_volumetric_data',
    'read_angles',
    'write_angles',
    'read_qm_metadata',
    'read_qm_rundata',
    'read_timestep',
    'read_timestep_metadata',
    'read_qm_timestep_metadata',
    'cons_fputs',
]
struct_anon_222._fields_ = [
    ('abiversion', c_int),
    ('type', String),
    ('name', String),
    ('prettyname', String),
    ('author', String),
    ('majorv', c_int),
    ('minorv', c_int),
    ('is_reentrant', c_int),
    ('filename_extension', String),
    ('open_file_read', CFUNCTYPE(UNCHECKED(POINTER(None)), String, String, POINTER(c_int))),
    ('read_structure', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_int), POINTER(molfile_atom_t))),
    ('read_bonds', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(POINTER(c_int)), POINTER(POINTER(c_float)), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(POINTER(c_char))))),
    ('read_next_timestep', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int, POINTER(molfile_timestep_t))),
    ('close_file_read', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('open_file_write', CFUNCTYPE(UNCHECKED(POINTER(None)), String, String, c_int)),
    ('write_structure', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int, POINTER(molfile_atom_t))),
    ('write_timestep', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(molfile_timestep_t))),
    ('close_file_write', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('read_volumetric_metadata', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_int), POINTER(POINTER(molfile_volumetric_t)))),
    ('read_volumetric_data', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int, POINTER(c_float), POINTER(c_float))),
    ('read_rawgraphics', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_int), POINTER(POINTER(molfile_graphics_t)))),
    ('read_molecule_metadata', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(POINTER(molfile_metadata_t)))),
    ('write_bonds', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_float), POINTER(c_int), c_int, POINTER(POINTER(c_char)))),
    ('write_volumetric_data', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(molfile_volumetric_t), POINTER(c_float), POINTER(c_float))),
    ('read_angles', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(POINTER(c_char))), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(POINTER(c_char))), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(POINTER(POINTER(c_char))), POINTER(c_int), POINTER(POINTER(c_int)), POINTER(c_int), POINTER(c_int))),
    ('write_angles', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int, POINTER(c_int), POINTER(c_int), c_int, POINTER(POINTER(c_char)), c_int, POINTER(c_int), POINTER(c_int), c_int, POINTER(POINTER(c_char)), c_int, POINTER(c_int), POINTER(c_int), c_int, POINTER(POINTER(c_char)), c_int, POINTER(c_int), c_int, c_int)),
    ('read_qm_metadata', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(molfile_qm_metadata_t))),
    ('read_qm_rundata', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(molfile_qm_t))),
    ('read_timestep', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_int, POINTER(molfile_timestep_t), POINTER(molfile_qm_metadata_t), POINTER(molfile_qm_timestep_t))),
    ('read_timestep_metadata', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(molfile_timestep_metadata_t))),
    ('read_qm_timestep_metadata', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(molfile_qm_timestep_metadata_t))),
    ('cons_fputs', CFUNCTYPE(UNCHECKED(c_int), c_int, String)),
]

molfile_plugin_t = struct_anon_222 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../molfile_plugin.h: 810

# /home/piton/scr/gromacs-4.5.5/include/types/../types/trx.h: 49
class struct_trxframe(Structure):
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/../vmdio.h: 37
class struct_anon_223(Structure):
    pass

struct_anon_223.__slots__ = [
    'api',
    'filetype',
    'handle',
    'bV',
]
struct_anon_223._fields_ = [
    ('api', POINTER(molfile_plugin_t)),
    ('filetype', String),
    ('handle', POINTER(None)),
    ('bV', gmx_bool),
]

t_gmxvmdplugin = struct_anon_223 # /home/piton/scr/gromacs-4.5.5/include/types/../types/../vmdio.h: 37

struct_trxframe.__slots__ = [
    'flags',
    'not_ok',
    'bDouble',
    'natoms',
    't0',
    'tpf',
    'tppf',
    'bTitle',
    'title',
    'bStep',
    'step',
    'bTime',
    'time',
    'bLambda',
    '_lambda',
    'bAtoms',
    'atoms',
    'bPrec',
    'prec',
    'bX',
    'x',
    'bV',
    'v',
    'bF',
    'f',
    'bBox',
    'box',
    'bPBC',
    'ePBC',
    'vmdplugin',
]
struct_trxframe._fields_ = [
    ('flags', c_int),
    ('not_ok', c_int),
    ('bDouble', gmx_bool),
    ('natoms', c_int),
    ('t0', real),
    ('tpf', real),
    ('tppf', real),
    ('bTitle', gmx_bool),
    ('title', String),
    ('bStep', gmx_bool),
    ('step', c_int),
    ('bTime', gmx_bool),
    ('time', real),
    ('bLambda', gmx_bool),
    ('_lambda', real),
    ('bAtoms', gmx_bool),
    ('atoms', POINTER(t_atoms)),
    ('bPrec', gmx_bool),
    ('prec', real),
    ('bX', gmx_bool),
    ('x', POINTER(rvec)),
    ('bV', gmx_bool),
    ('v', POINTER(rvec)),
    ('bF', gmx_bool),
    ('f', POINTER(rvec)),
    ('bBox', gmx_bool),
    ('box', matrix),
    ('bPBC', gmx_bool),
    ('ePBC', c_int),
    ('vmdplugin', t_gmxvmdplugin),
]

t_trxframe = struct_trxframe # /home/piton/scr/gromacs-4.5.5/include/types/../types/trx.h: 85

enum_anon_224 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcTC = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcENER = (egcTC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcACC = (egcENER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcFREEZE = (egcACC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcUser1 = (egcFREEZE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcUser2 = (egcUser1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcVCM = (egcUser2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcXTC = (egcVCM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcORFIT = (egcXTC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcQMMM = (egcORFIT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

egcNR = (egcQMMM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 46

# /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 59
class struct_anon_225(Structure):
    pass

struct_anon_225.__slots__ = [
    'name',
    'atoms',
    'ilist',
    'cgs',
    'excls',
]
struct_anon_225._fields_ = [
    ('name', POINTER(POINTER(c_char))),
    ('atoms', t_atoms),
    ('ilist', t_ilist * F_NRE),
    ('cgs', t_block),
    ('excls', t_blocka),
]

gmx_moltype_t = struct_anon_225 # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 59

# /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 69
class struct_anon_226(Structure):
    pass

struct_anon_226.__slots__ = [
    'type',
    'nmol',
    'natoms_mol',
    'nposres_xA',
    'posres_xA',
    'nposres_xB',
    'posres_xB',
]
struct_anon_226._fields_ = [
    ('type', c_int),
    ('nmol', c_int),
    ('natoms_mol', c_int),
    ('nposres_xA', c_int),
    ('posres_xA', POINTER(rvec)),
    ('nposres_xB', c_int),
    ('posres_xB', POINTER(rvec)),
]

gmx_molblock_t = struct_anon_226 # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 69

# /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 77
class struct_anon_227(Structure):
    pass

struct_anon_227.__slots__ = [
    'grps',
    'ngrpname',
    'grpname',
    'ngrpnr',
    'grpnr',
]
struct_anon_227._fields_ = [
    ('grps', t_grps * egcNR),
    ('ngrpname', c_int),
    ('grpname', POINTER(POINTER(POINTER(c_char)))),
    ('ngrpnr', c_int * egcNR),
    ('grpnr', POINTER(c_ubyte) * egcNR),
]

gmx_groups_t = struct_anon_227 # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 77

# /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 101
class struct_anon_228(Structure):
    pass

struct_anon_228.__slots__ = [
    'name',
    'ffparams',
    'nmoltype',
    'moltype',
    'nmolblock',
    'molblock',
    'natoms',
    'maxres_renum',
    'maxresnr',
    'atomtypes',
    'mols',
    'groups',
    'symtab',
]
struct_anon_228._fields_ = [
    ('name', POINTER(POINTER(c_char))),
    ('ffparams', gmx_ffparams_t),
    ('nmoltype', c_int),
    ('moltype', POINTER(gmx_moltype_t)),
    ('nmolblock', c_int),
    ('molblock', POINTER(gmx_molblock_t)),
    ('natoms', c_int),
    ('maxres_renum', c_int),
    ('maxresnr', c_int),
    ('atomtypes', t_atomtypes),
    ('mols', t_block),
    ('groups', gmx_groups_t),
    ('symtab', t_symtab),
]

gmx_mtop_t = struct_anon_228 # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 101

# /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 109
class struct_anon_229(Structure):
    pass

struct_anon_229.__slots__ = [
    'idef',
    'atomtypes',
    'cgs',
    'excls',
]
struct_anon_229._fields_ = [
    ('idef', t_idef),
    ('atomtypes', t_atomtypes),
    ('cgs', t_block),
    ('excls', t_blocka),
]

gmx_localtop_t = struct_anon_229 # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 109

# /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 121
class struct_anon_230(Structure):
    pass

struct_anon_230.__slots__ = [
    'name',
    'idef',
    'atoms',
    'atomtypes',
    'cgs',
    'mols',
    'excls',
    'symtab',
]
struct_anon_230._fields_ = [
    ('name', POINTER(POINTER(c_char))),
    ('idef', t_idef),
    ('atoms', t_atoms),
    ('atomtypes', t_atomtypes),
    ('cgs', t_block),
    ('mols', t_block),
    ('excls', t_blocka),
    ('symtab', t_symtab),
]

t_topology = struct_anon_230 # /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 121

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 51
class struct_anon_231(Structure):
    pass

struct_anon_231.__slots__ = [
    'n',
    'a',
    'phi',
]
struct_anon_231._fields_ = [
    ('n', c_int),
    ('a', POINTER(real)),
    ('phi', POINTER(real)),
]

t_cosines = struct_anon_231 # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 51

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 58
class struct_anon_232(Structure):
    pass

struct_anon_232.__slots__ = [
    'E0',
    'omega',
    't0',
    'sigma',
]
struct_anon_232._fields_ = [
    ('E0', real),
    ('omega', real),
    ('t0', real),
    ('sigma', real),
]

t_efield = struct_anon_232 # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 58

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 95
class struct_anon_233(Structure):
    pass

struct_anon_233.__slots__ = [
    'ngtc',
    'nhchainlength',
    'ngacc',
    'ngfrz',
    'ngener',
    'nrdf',
    'ref_t',
    'annealing',
    'anneal_npoints',
    'anneal_time',
    'anneal_temp',
    'tau_t',
    'acc',
    'nFreeze',
    'egp_flags',
    'ngQM',
    'QMmethod',
    'QMbasis',
    'QMcharge',
    'QMmult',
    'bSH',
    'CASorbitals',
    'CASelectrons',
    'SAon',
    'SAoff',
    'SAsteps',
    'bOPT',
    'bTS',
]
struct_anon_233._fields_ = [
    ('ngtc', c_int),
    ('nhchainlength', c_int),
    ('ngacc', c_int),
    ('ngfrz', c_int),
    ('ngener', c_int),
    ('nrdf', POINTER(real)),
    ('ref_t', POINTER(real)),
    ('annealing', POINTER(c_int)),
    ('anneal_npoints', POINTER(c_int)),
    ('anneal_time', POINTER(POINTER(real))),
    ('anneal_temp', POINTER(POINTER(real))),
    ('tau_t', POINTER(real)),
    ('acc', POINTER(rvec)),
    ('nFreeze', POINTER(ivec)),
    ('egp_flags', POINTER(c_int)),
    ('ngQM', c_int),
    ('QMmethod', POINTER(c_int)),
    ('QMbasis', POINTER(c_int)),
    ('QMcharge', POINTER(c_int)),
    ('QMmult', POINTER(c_int)),
    ('bSH', POINTER(gmx_bool)),
    ('CASorbitals', POINTER(c_int)),
    ('CASelectrons', POINTER(c_int)),
    ('SAon', POINTER(real)),
    ('SAoff', POINTER(real)),
    ('SAsteps', POINTER(c_int)),
    ('bOPT', POINTER(gmx_bool)),
    ('bTS', POINTER(gmx_bool)),
]

t_grpopts = struct_anon_233 # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 95

enum_anon_234 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 97

epgrppbcNONE = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 97

epgrppbcREFAT = (epgrppbcNONE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 97

epgrppbcCOS = (epgrppbcREFAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 97

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 122
class struct_anon_235(Structure):
    pass

struct_anon_235.__slots__ = [
    'nat',
    'ind',
    'nat_loc',
    'nalloc_loc',
    'ind_loc',
    'nweight',
    'weight',
    'weight_loc',
    'epgrppbc',
    'pbcatom',
    'vec',
    'init',
    'rate',
    'k',
    'kB',
    'wscale',
    'invtm',
    'x',
    'xp',
    'dr',
    'f_scal',
    'f',
]
struct_anon_235._fields_ = [
    ('nat', c_int),
    ('ind', POINTER(atom_id)),
    ('nat_loc', c_int),
    ('nalloc_loc', c_int),
    ('ind_loc', POINTER(atom_id)),
    ('nweight', c_int),
    ('weight', POINTER(real)),
    ('weight_loc', POINTER(real)),
    ('epgrppbc', c_int),
    ('pbcatom', atom_id),
    ('vec', rvec),
    ('init', rvec),
    ('rate', real),
    ('k', real),
    ('kB', real),
    ('wscale', real),
    ('invtm', real),
    ('x', dvec),
    ('xp', dvec),
    ('dr', dvec),
    ('f_scal', c_double),
    ('f', dvec),
]

t_pullgrp = struct_anon_235 # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 122

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 146
class struct_anon_236(Structure):
    pass

struct_anon_236.__slots__ = [
    'ngrp',
    'eGeom',
    'dim',
    'cyl_r1',
    'cyl_r0',
    'constr_tol',
    'nstxout',
    'nstfout',
    'ePBC',
    'npbcdim',
    'bRefAt',
    'cosdim',
    'bVirial',
    'grp',
    'dyna',
    'rbuf',
    'dbuf',
    'dbuf_cyl',
    'out_x',
    'out_f',
]
struct_anon_236._fields_ = [
    ('ngrp', c_int),
    ('eGeom', c_int),
    ('dim', ivec),
    ('cyl_r1', real),
    ('cyl_r0', real),
    ('constr_tol', real),
    ('nstxout', c_int),
    ('nstfout', c_int),
    ('ePBC', c_int),
    ('npbcdim', c_int),
    ('bRefAt', gmx_bool),
    ('cosdim', c_int),
    ('bVirial', gmx_bool),
    ('grp', POINTER(t_pullgrp)),
    ('dyna', POINTER(t_pullgrp)),
    ('rbuf', POINTER(rvec)),
    ('dbuf', POINTER(dvec)),
    ('dbuf_cyl', POINTER(c_double)),
    ('out_x', POINTER(FILE)),
    ('out_f', POINTER(FILE)),
]

t_pull = struct_anon_236 # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 146

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 287
class struct_anon_237(Structure):
    pass

struct_anon_237.__slots__ = [
    'eI',
    'nsteps',
    'simulation_part',
    'init_step',
    'nstcalcenergy',
    'ns_type',
    'nstlist',
    'ndelta',
    'nstcomm',
    'comm_mode',
    'nstcheckpoint',
    'nstlog',
    'nstxout',
    'nstvout',
    'nstfout',
    'nstenergy',
    'nstxtcout',
    'init_t',
    'delta_t',
    'xtcprec',
    'nkx',
    'nky',
    'nkz',
    'pme_order',
    'ewald_rtol',
    'ewald_geometry',
    'epsilon_surface',
    'bOptFFT',
    'ePBC',
    'bPeriodicMols',
    'bContinuation',
    'etc',
    'nsttcouple',
    'epc',
    'epct',
    'nstpcouple',
    'tau_p',
    'ref_p',
    'compress',
    'refcoord_scaling',
    'posres_com',
    'posres_comB',
    'andersen_seed',
    'rlist',
    'rlistlong',
    'rtpi',
    'coulombtype',
    'rcoulomb_switch',
    'rcoulomb',
    'epsilon_r',
    'epsilon_rf',
    'implicit_solvent',
    'gb_algorithm',
    'nstgbradii',
    'rgbradii',
    'gb_saltconc',
    'gb_epsilon_solvent',
    'gb_obc_alpha',
    'gb_obc_beta',
    'gb_obc_gamma',
    'gb_dielectric_offset',
    'sa_algorithm',
    'sa_surface_tension',
    'vdwtype',
    'rvdw_switch',
    'rvdw',
    'eDispCorr',
    'tabext',
    'shake_tol',
    'efep',
    'init_lambda',
    'delta_lambda',
    'n_flambda',
    'flambda',
    'sc_alpha',
    'sc_power',
    'sc_sigma',
    'sc_sigma_min',
    'nstdhdl',
    'separate_dhdl_file',
    'dhdl_derivatives',
    'dh_hist_size',
    'dh_hist_spacing',
    'eDisre',
    'dr_fc',
    'eDisreWeighting',
    'bDisreMixed',
    'nstdisreout',
    'dr_tau',
    'orires_fc',
    'orires_tau',
    'nstorireout',
    'dihre_fc',
    'em_stepsize',
    'em_tol',
    'niter',
    'fc_stepsize',
    'nstcgsteep',
    'nbfgscorr',
    'eConstrAlg',
    'nProjOrder',
    'LincsWarnAngle',
    'nLincsIter',
    'bShakeSOR',
    'bd_fric',
    'ld_seed',
    'nwall',
    'wall_type',
    'wall_r_linpot',
    'wall_atomtype',
    'wall_density',
    'wall_ewald_zfac',
    'ePull',
    'pull',
    'cos_accel',
    'deform',
    'userint1',
    'userint2',
    'userint3',
    'userint4',
    'userreal1',
    'userreal2',
    'userreal3',
    'userreal4',
    'opts',
    'ex',
    'et',
    'bQMMM',
    'QMconstraints',
    'QMMMscheme',
    'scalefactor',
]
struct_anon_237._fields_ = [
    ('eI', c_int),
    ('nsteps', gmx_large_int_t),
    ('simulation_part', c_int),
    ('init_step', gmx_large_int_t),
    ('nstcalcenergy', c_int),
    ('ns_type', c_int),
    ('nstlist', c_int),
    ('ndelta', c_int),
    ('nstcomm', c_int),
    ('comm_mode', c_int),
    ('nstcheckpoint', c_int),
    ('nstlog', c_int),
    ('nstxout', c_int),
    ('nstvout', c_int),
    ('nstfout', c_int),
    ('nstenergy', c_int),
    ('nstxtcout', c_int),
    ('init_t', c_double),
    ('delta_t', c_double),
    ('xtcprec', real),
    ('nkx', c_int),
    ('nky', c_int),
    ('nkz', c_int),
    ('pme_order', c_int),
    ('ewald_rtol', real),
    ('ewald_geometry', c_int),
    ('epsilon_surface', real),
    ('bOptFFT', gmx_bool),
    ('ePBC', c_int),
    ('bPeriodicMols', c_int),
    ('bContinuation', gmx_bool),
    ('etc', c_int),
    ('nsttcouple', c_int),
    ('epc', c_int),
    ('epct', c_int),
    ('nstpcouple', c_int),
    ('tau_p', real),
    ('ref_p', tensor),
    ('compress', tensor),
    ('refcoord_scaling', c_int),
    ('posres_com', rvec),
    ('posres_comB', rvec),
    ('andersen_seed', c_int),
    ('rlist', real),
    ('rlistlong', real),
    ('rtpi', real),
    ('coulombtype', c_int),
    ('rcoulomb_switch', real),
    ('rcoulomb', real),
    ('epsilon_r', real),
    ('epsilon_rf', real),
    ('implicit_solvent', c_int),
    ('gb_algorithm', c_int),
    ('nstgbradii', c_int),
    ('rgbradii', real),
    ('gb_saltconc', real),
    ('gb_epsilon_solvent', real),
    ('gb_obc_alpha', real),
    ('gb_obc_beta', real),
    ('gb_obc_gamma', real),
    ('gb_dielectric_offset', real),
    ('sa_algorithm', c_int),
    ('sa_surface_tension', real),
    ('vdwtype', c_int),
    ('rvdw_switch', real),
    ('rvdw', real),
    ('eDispCorr', c_int),
    ('tabext', real),
    ('shake_tol', real),
    ('efep', c_int),
    ('init_lambda', c_double),
    ('delta_lambda', c_double),
    ('n_flambda', c_int),
    ('flambda', POINTER(c_double)),
    ('sc_alpha', real),
    ('sc_power', c_int),
    ('sc_sigma', real),
    ('sc_sigma_min', real),
    ('nstdhdl', c_int),
    ('separate_dhdl_file', c_int),
    ('dhdl_derivatives', c_int),
    ('dh_hist_size', c_int),
    ('dh_hist_spacing', c_double),
    ('eDisre', c_int),
    ('dr_fc', real),
    ('eDisreWeighting', c_int),
    ('bDisreMixed', gmx_bool),
    ('nstdisreout', c_int),
    ('dr_tau', real),
    ('orires_fc', real),
    ('orires_tau', real),
    ('nstorireout', c_int),
    ('dihre_fc', real),
    ('em_stepsize', real),
    ('em_tol', real),
    ('niter', c_int),
    ('fc_stepsize', real),
    ('nstcgsteep', c_int),
    ('nbfgscorr', c_int),
    ('eConstrAlg', c_int),
    ('nProjOrder', c_int),
    ('LincsWarnAngle', real),
    ('nLincsIter', c_int),
    ('bShakeSOR', gmx_bool),
    ('bd_fric', real),
    ('ld_seed', c_int),
    ('nwall', c_int),
    ('wall_type', c_int),
    ('wall_r_linpot', real),
    ('wall_atomtype', c_int * 2),
    ('wall_density', real * 2),
    ('wall_ewald_zfac', real),
    ('ePull', c_int),
    ('pull', POINTER(t_pull)),
    ('cos_accel', real),
    ('deform', tensor),
    ('userint1', c_int),
    ('userint2', c_int),
    ('userint3', c_int),
    ('userint4', c_int),
    ('userreal1', real),
    ('userreal2', real),
    ('userreal3', real),
    ('userreal4', real),
    ('opts', t_grpopts),
    ('ex', t_cosines * 3),
    ('et', t_cosines * 3),
    ('bQMMM', gmx_bool),
    ('QMconstraints', c_int),
    ('QMMMscheme', c_int),
    ('scalefactor', real),
]

t_inputrec = struct_anon_237 # /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 287

enum_anon_238 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL010 = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL020 = (eNR_NBKERNEL010 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL030 = (eNR_NBKERNEL020 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL100 = (eNR_NBKERNEL030 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL101 = (eNR_NBKERNEL100 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL102 = (eNR_NBKERNEL101 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL103 = (eNR_NBKERNEL102 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL104 = (eNR_NBKERNEL103 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL110 = (eNR_NBKERNEL104 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL111 = (eNR_NBKERNEL110 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL112 = (eNR_NBKERNEL111 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL113 = (eNR_NBKERNEL112 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL114 = (eNR_NBKERNEL113 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL120 = (eNR_NBKERNEL114 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL121 = (eNR_NBKERNEL120 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL122 = (eNR_NBKERNEL121 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL123 = (eNR_NBKERNEL122 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL124 = (eNR_NBKERNEL123 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL130 = (eNR_NBKERNEL124 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL131 = (eNR_NBKERNEL130 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL132 = (eNR_NBKERNEL131 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL133 = (eNR_NBKERNEL132 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL134 = (eNR_NBKERNEL133 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL200 = (eNR_NBKERNEL134 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL201 = (eNR_NBKERNEL200 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL202 = (eNR_NBKERNEL201 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL203 = (eNR_NBKERNEL202 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL204 = (eNR_NBKERNEL203 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL210 = (eNR_NBKERNEL204 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL211 = (eNR_NBKERNEL210 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL212 = (eNR_NBKERNEL211 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL213 = (eNR_NBKERNEL212 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL214 = (eNR_NBKERNEL213 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL220 = (eNR_NBKERNEL214 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL221 = (eNR_NBKERNEL220 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL222 = (eNR_NBKERNEL221 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL223 = (eNR_NBKERNEL222 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL224 = (eNR_NBKERNEL223 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL230 = (eNR_NBKERNEL224 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL231 = (eNR_NBKERNEL230 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL232 = (eNR_NBKERNEL231 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL233 = (eNR_NBKERNEL232 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL234 = (eNR_NBKERNEL233 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL300 = (eNR_NBKERNEL234 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL301 = (eNR_NBKERNEL300 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL302 = (eNR_NBKERNEL301 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL303 = (eNR_NBKERNEL302 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL304 = (eNR_NBKERNEL303 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL310 = (eNR_NBKERNEL304 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL311 = (eNR_NBKERNEL310 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL312 = (eNR_NBKERNEL311 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL313 = (eNR_NBKERNEL312 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL314 = (eNR_NBKERNEL313 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL320 = (eNR_NBKERNEL314 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL321 = (eNR_NBKERNEL320 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL322 = (eNR_NBKERNEL321 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL323 = (eNR_NBKERNEL322 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL324 = (eNR_NBKERNEL323 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL330 = (eNR_NBKERNEL324 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL331 = (eNR_NBKERNEL330 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL332 = (eNR_NBKERNEL331 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL333 = (eNR_NBKERNEL332 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL334 = (eNR_NBKERNEL333 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL400 = (eNR_NBKERNEL334 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL410 = (eNR_NBKERNEL400 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL430 = (eNR_NBKERNEL410 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL010NF = (eNR_NBKERNEL430 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL020NF = (eNR_NBKERNEL010NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL030NF = (eNR_NBKERNEL020NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL100NF = (eNR_NBKERNEL030NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL101NF = (eNR_NBKERNEL100NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL102NF = (eNR_NBKERNEL101NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL103NF = (eNR_NBKERNEL102NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL104NF = (eNR_NBKERNEL103NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL110NF = (eNR_NBKERNEL104NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL111NF = (eNR_NBKERNEL110NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL112NF = (eNR_NBKERNEL111NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL113NF = (eNR_NBKERNEL112NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL114NF = (eNR_NBKERNEL113NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL120NF = (eNR_NBKERNEL114NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL121NF = (eNR_NBKERNEL120NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL122NF = (eNR_NBKERNEL121NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL123NF = (eNR_NBKERNEL122NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL124NF = (eNR_NBKERNEL123NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL130NF = (eNR_NBKERNEL124NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL131NF = (eNR_NBKERNEL130NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL132NF = (eNR_NBKERNEL131NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL133NF = (eNR_NBKERNEL132NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL134NF = (eNR_NBKERNEL133NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL200NF = (eNR_NBKERNEL134NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL201NF = (eNR_NBKERNEL200NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL202NF = (eNR_NBKERNEL201NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL203NF = (eNR_NBKERNEL202NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL204NF = (eNR_NBKERNEL203NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL210NF = (eNR_NBKERNEL204NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL211NF = (eNR_NBKERNEL210NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL212NF = (eNR_NBKERNEL211NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL213NF = (eNR_NBKERNEL212NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL214NF = (eNR_NBKERNEL213NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL220NF = (eNR_NBKERNEL214NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL221NF = (eNR_NBKERNEL220NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL222NF = (eNR_NBKERNEL221NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL223NF = (eNR_NBKERNEL222NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL224NF = (eNR_NBKERNEL223NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL230NF = (eNR_NBKERNEL224NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL231NF = (eNR_NBKERNEL230NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL232NF = (eNR_NBKERNEL231NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL233NF = (eNR_NBKERNEL232NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL234NF = (eNR_NBKERNEL233NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL300NF = (eNR_NBKERNEL234NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL301NF = (eNR_NBKERNEL300NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL302NF = (eNR_NBKERNEL301NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL303NF = (eNR_NBKERNEL302NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL304NF = (eNR_NBKERNEL303NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL310NF = (eNR_NBKERNEL304NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL311NF = (eNR_NBKERNEL310NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL312NF = (eNR_NBKERNEL311NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL313NF = (eNR_NBKERNEL312NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL314NF = (eNR_NBKERNEL313NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL320NF = (eNR_NBKERNEL314NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL321NF = (eNR_NBKERNEL320NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL322NF = (eNR_NBKERNEL321NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL323NF = (eNR_NBKERNEL322NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL324NF = (eNR_NBKERNEL323NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL330NF = (eNR_NBKERNEL324NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL331NF = (eNR_NBKERNEL330NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL332NF = (eNR_NBKERNEL331NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL333NF = (eNR_NBKERNEL332NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL334NF = (eNR_NBKERNEL333NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL400NF = (eNR_NBKERNEL334NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL410NF = (eNR_NBKERNEL400NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL430NF = (eNR_NBKERNEL410NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL_NR = (eNR_NBKERNEL430NF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL_FREE_ENERGY = eNR_NBKERNEL_NR # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL_ALLVSALL = (eNR_NBKERNEL_FREE_ENERGY + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL_ALLVSALLGB = (eNR_NBKERNEL_ALLVSALL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NBKERNEL_OUTER = (eNR_NBKERNEL_ALLVSALLGB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NB14 = (eNR_NBKERNEL_OUTER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_BORN_RADII_STILL = (eNR_NB14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_BORN_RADII_HCT_OBC = (eNR_BORN_RADII_STILL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_BORN_CHAINRULE = (eNR_BORN_RADII_HCT_OBC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_BORN_AVA_RADII_STILL = (eNR_BORN_CHAINRULE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_BORN_AVA_RADII_HCT_OBC = (eNR_BORN_AVA_RADII_STILL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_BORN_AVA_CHAINRULE = (eNR_BORN_AVA_RADII_HCT_OBC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_WEIGHTS = (eNR_BORN_AVA_CHAINRULE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_SPREADQ = (eNR_WEIGHTS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_SPREADQBSP = (eNR_SPREADQ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_GATHERF = (eNR_SPREADQBSP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_GATHERFBSP = (eNR_GATHERF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_FFT = (eNR_GATHERFBSP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_CONV = (eNR_FFT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_SOLVEPME = (eNR_CONV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_NS = (eNR_SOLVEPME + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_RESETX = (eNR_NS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_SHIFTX = (eNR_RESETX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_CGCM = (eNR_SHIFTX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_FSUM = (eNR_CGCM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_BONDS = (eNR_FSUM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_G96BONDS = (eNR_BONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_FENEBONDS = (eNR_G96BONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_TABBONDS = (eNR_FENEBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_RESTRBONDS = (eNR_TABBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_ANGLES = (eNR_RESTRBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_G96ANGLES = (eNR_ANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_QANGLES = (eNR_G96ANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_TABANGLES = (eNR_QANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_PROPER = (eNR_TABANGLES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_IMPROPER = (eNR_PROPER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_RB = (eNR_IMPROPER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_FOURDIH = (eNR_RB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_TABDIHS = (eNR_FOURDIH + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_DISRES = (eNR_TABDIHS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_ORIRES = (eNR_DISRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_DIHRES = (eNR_ORIRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_POSRES = (eNR_DIHRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_ANGRES = (eNR_POSRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_ANGRESZ = (eNR_ANGRES + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_MORSE = (eNR_ANGRESZ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_CUBICBONDS = (eNR_MORSE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_WALLS = (eNR_CUBICBONDS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_WPOL = (eNR_WALLS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_THOLE = (eNR_WPOL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VIRIAL = (eNR_THOLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_UPDATE = (eNR_VIRIAL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_EXTUPDATE = (eNR_UPDATE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_STOPCM = (eNR_EXTUPDATE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_PCOUPL = (eNR_STOPCM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_EKIN = (eNR_PCOUPL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_LINCS = (eNR_EKIN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_LINCSMAT = (eNR_LINCS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_SHAKE = (eNR_LINCSMAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_CONSTR_V = (eNR_SHAKE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_SHAKE_RIJ = (eNR_CONSTR_V + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_CONSTR_VIR = (eNR_SHAKE_RIJ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_SETTLE = (eNR_CONSTR_VIR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITE2 = (eNR_SETTLE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITE3 = (eNR_VSITE2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITE3FD = (eNR_VSITE3 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITE3FAD = (eNR_VSITE3FD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITE3OUT = (eNR_VSITE3FAD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITE4FD = (eNR_VSITE3OUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITE4FDN = (eNR_VSITE4FD + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_VSITEN = (eNR_VSITE4FDN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_GB = (eNR_VSITEN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNR_CMAP = (eNR_GB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

eNRNB = (eNR_CMAP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 58

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 125
class struct_anon_239(Structure):
    pass

struct_anon_239.__slots__ = [
    'n',
]
struct_anon_239._fields_ = [
    ('n', c_double * eNRNB),
]

t_nrnb = struct_anon_239 # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 125

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 128
class struct_gmx_wallcycle(Structure):
    pass

gmx_wallcycle_t = POINTER(struct_gmx_wallcycle) # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 128

enum_anon_240 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_VDWQQ = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_VDW = (eNL_VDWQQ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_QQ = (eNL_VDW + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_VDWQQ_FREE = (eNL_QQ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_VDW_FREE = (eNL_VDWQQ_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_QQ_FREE = (eNL_VDW_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_VDWQQ_WATER = (eNL_QQ_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_QQ_WATER = (eNL_VDWQQ_WATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_VDWQQ_WATERWATER = (eNL_QQ_WATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_QQ_WATERWATER = (eNL_VDWQQ_WATERWATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

eNL_NR = (eNL_QQ_WATERWATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 42

enum_anon_241 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egCOULSR = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egLJSR = (egCOULSR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egBHAMSR = (egLJSR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egCOULLR = (egBHAMSR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egLJLR = (egCOULLR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egBHAMLR = (egLJLR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egCOUL14 = (egBHAMLR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egLJ14 = (egCOUL14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egGB = (egLJ14 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

egNR = (egGB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 99

# /home/piton/scr/gromacs-4.5.5/include/types/../types/mdatom.h: 69
class struct_anon_242(Structure):
    pass

struct_anon_242.__slots__ = [
    'tmassA',
    'tmassB',
    'tmass',
    'nr',
    'nalloc',
    'nenergrp',
    'bVCMgrps',
    'nPerturbed',
    'nMassPerturbed',
    'nChargePerturbed',
    'bOrires',
    'massA',
    'massB',
    'massT',
    'invmass',
    'chargeA',
    'chargeB',
    'bPerturbed',
    'typeA',
    'typeB',
    'ptype',
    'cTC',
    'cENER',
    'cACC',
    'cFREEZE',
    'cVCM',
    'cU1',
    'cU2',
    'cORF',
    'bQM',
    'start',
    'homenr',
    '_lambda',
]
struct_anon_242._fields_ = [
    ('tmassA', real),
    ('tmassB', real),
    ('tmass', real),
    ('nr', c_int),
    ('nalloc', c_int),
    ('nenergrp', c_int),
    ('bVCMgrps', gmx_bool),
    ('nPerturbed', c_int),
    ('nMassPerturbed', c_int),
    ('nChargePerturbed', c_int),
    ('bOrires', gmx_bool),
    ('massA', POINTER(real)),
    ('massB', POINTER(real)),
    ('massT', POINTER(real)),
    ('invmass', POINTER(real)),
    ('chargeA', POINTER(real)),
    ('chargeB', POINTER(real)),
    ('bPerturbed', POINTER(gmx_bool)),
    ('typeA', POINTER(c_int)),
    ('typeB', POINTER(c_int)),
    ('ptype', POINTER(c_ushort)),
    ('cTC', POINTER(c_ushort)),
    ('cENER', POINTER(c_ushort)),
    ('cACC', POINTER(c_ushort)),
    ('cFREEZE', POINTER(c_ushort)),
    ('cVCM', POINTER(c_ushort)),
    ('cU1', POINTER(c_ushort)),
    ('cU2', POINTER(c_ushort)),
    ('cORF', POINTER(c_ushort)),
    ('bQM', POINTER(gmx_bool)),
    ('start', c_int),
    ('homenr', c_int),
    ('_lambda', real),
]

t_mdatoms = struct_anon_242 # /home/piton/scr/gromacs-4.5.5/include/types/../types/mdatom.h: 69

# /home/piton/scr/gromacs-4.5.5/include/types/../types/pbc.h: 65
class struct_anon_243(Structure):
    pass

struct_anon_243.__slots__ = [
    'ndim_ePBC',
    'ePBCDX',
    'dim',
    'box',
    'fbox_diag',
    'hbox_diag',
    'mhbox_diag',
    'max_cutoff2',
    'bLimitDistance',
    'limit_distance2',
    'ntric_vec',
    'tric_shift',
    'tric_vec',
]
struct_anon_243._fields_ = [
    ('ndim_ePBC', c_int),
    ('ePBCDX', c_int),
    ('dim', c_int),
    ('box', matrix),
    ('fbox_diag', rvec),
    ('hbox_diag', rvec),
    ('mhbox_diag', rvec),
    ('max_cutoff2', real),
    ('bLimitDistance', gmx_bool),
    ('limit_distance2', real),
    ('ntric_vec', c_int),
    ('tric_shift', ivec * 12),
    ('tric_vec', rvec * 12),
]

t_pbc = struct_anon_243 # /home/piton/scr/gromacs-4.5.5/include/types/../types/pbc.h: 65

enum_anon_244 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efMDP = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efGCT = (efMDP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTRX = (efGCT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTRO = (efTRX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTRN = (efTRO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTRR = (efTRN + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTRJ = (efTRR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efXTC = (efTRJ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efG87 = (efXTC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efEDR = (efG87 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efSTX = (efEDR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efSTO = (efSTX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efGRO = (efSTO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efG96 = (efGRO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efPDB = (efG96 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efBRK = (efPDB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efENT = (efBRK + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efESP = (efENT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efPQR = (efESP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efXYZ = (efPQR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efCPT = (efXYZ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efLOG = (efCPT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efXVG = (efLOG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efOUT = (efXVG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efNDX = (efOUT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTOP = (efNDX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efITP = (efTOP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTPX = (efITP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTPS = (efTPX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTPR = (efTPS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTPA = (efTPR + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTPB = (efTPA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efTEX = (efTPB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efRTP = (efTEX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efATP = (efRTP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efHDB = (efATP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efDAT = (efHDB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efDLG = (efDAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efMAP = (efDLG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efEPS = (efMAP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efMAT = (efEPS + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efM2P = (efMAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efMTX = (efM2P + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efEDI = (efMTX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efEDO = (efEDI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efHAT = (efEDO + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efCUB = (efHAT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efXPM = (efCUB + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efRND = (efXPM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

efNR = (efRND + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 42

enum_anon_245 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estLAMBDA = 0 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estBOX = (estLAMBDA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estBOX_REL = (estBOX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estBOXV = (estBOX_REL + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estPRES_PREV = (estBOXV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estNH_XI = (estPRES_PREV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estTC_INT = (estNH_XI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estX = (estTC_INT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estV = (estX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estSDX = (estV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estCGP = (estSDX + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estLD_RNG = (estCGP + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estLD_RNGI = (estLD_RNG + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estDISRE_INITF = (estLD_RNGI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estDISRE_RM3TAV = (estDISRE_INITF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estORIRE_INITF = (estDISRE_RM3TAV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estORIRE_DTAV = (estORIRE_INITF + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estSVIR_PREV = (estORIRE_DTAV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estNH_VXI = (estSVIR_PREV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estVETA = (estNH_VXI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estVOL0 = (estVETA + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estNHPRES_XI = (estVOL0 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estNHPRES_VXI = (estNHPRES_XI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estFVIR_PREV = (estNHPRES_VXI + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

estNR = (estFVIR_PREV + 1) # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 58

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 69
for _lib in _libs.values():
    try:
        est_names = (POINTER(c_char) * estNR).in_dll(_lib, 'est_names')
        break
    except:
        pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 79
class struct_anon_246(Structure):
    pass

struct_anon_246.__slots__ = [
    'disre_initf',
    'ndisrepairs',
    'disre_rm3tav',
    'orire_initf',
    'norire_Dtav',
    'orire_Dtav',
]
struct_anon_246._fields_ = [
    ('disre_initf', real),
    ('ndisrepairs', c_int),
    ('disre_rm3tav', POINTER(real)),
    ('orire_initf', real),
    ('norire_Dtav', c_int),
    ('orire_Dtav', POINTER(real)),
]

history_t = struct_anon_246 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 79

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 100
class struct_anon_247(Structure):
    pass

struct_anon_247.__slots__ = [
    'bUpToDate',
    'ekin_n',
    'ekinh',
    'ekinf',
    'ekinh_old',
    'ekin_total',
    'ekinscalef_nhc',
    'ekinscaleh_nhc',
    'vscale_nhc',
    'dekindl',
    'mvcos',
]
struct_anon_247._fields_ = [
    ('bUpToDate', gmx_bool),
    ('ekin_n', c_int),
    ('ekinh', POINTER(tensor)),
    ('ekinf', POINTER(tensor)),
    ('ekinh_old', POINTER(tensor)),
    ('ekin_total', tensor),
    ('ekinscalef_nhc', POINTER(c_double)),
    ('ekinscaleh_nhc', POINTER(c_double)),
    ('vscale_nhc', POINTER(c_double)),
    ('dekindl', real),
    ('mvcos', real),
]

ekinstate_t = struct_anon_247 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 100

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 114
class struct_anon_248(Structure):
    pass

struct_anon_248.__slots__ = [
    'nndh',
    'ndh',
    'dh',
    'start_time',
    'start_lambda',
    'start_lambda_set',
]
struct_anon_248._fields_ = [
    ('nndh', c_int),
    ('ndh', POINTER(c_int)),
    ('dh', POINTER(POINTER(real))),
    ('start_time', c_double),
    ('start_lambda', c_double),
    ('start_lambda_set', gmx_bool),
]

delta_h_history_t = struct_anon_248 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 114

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 129
class struct_anon_249(Structure):
    pass

struct_anon_249.__slots__ = [
    'nsteps',
    'nsum',
    'ener_ave',
    'ener_sum',
    'nener',
    'nsteps_sim',
    'nsum_sim',
    'ener_sum_sim',
    'dht',
]
struct_anon_249._fields_ = [
    ('nsteps', gmx_large_int_t),
    ('nsum', gmx_large_int_t),
    ('ener_ave', POINTER(c_double)),
    ('ener_sum', POINTER(c_double)),
    ('nener', c_int),
    ('nsteps_sim', gmx_large_int_t),
    ('nsum_sim', gmx_large_int_t),
    ('ener_sum_sim', POINTER(c_double)),
    ('dht', POINTER(delta_h_history_t)),
]

energyhistory_t = struct_anon_249 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 129

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 174
class struct_anon_250(Structure):
    pass

struct_anon_250.__slots__ = [
    'natoms',
    'ngtc',
    'nnhpres',
    'nhchainlength',
    'nrng',
    'nrngi',
    'flags',
    '_lambda',
    'box',
    'box_rel',
    'boxv',
    'pres_prev',
    'svir_prev',
    'fvir_prev',
    'nosehoover_xi',
    'nosehoover_vxi',
    'nhpres_xi',
    'nhpres_vxi',
    'therm_integral',
    'veta',
    'vol0',
    'nalloc',
    'x',
    'v',
    'sd_X',
    'cg_p',
    'ld_rng',
    'ld_rngi',
    'hist',
    'ekinstate',
    'enerhist',
    'ddp_count',
    'ddp_count_cg_gl',
    'ncg_gl',
    'cg_gl',
    'cg_gl_nalloc',
]
struct_anon_250._fields_ = [
    ('natoms', c_int),
    ('ngtc', c_int),
    ('nnhpres', c_int),
    ('nhchainlength', c_int),
    ('nrng', c_int),
    ('nrngi', c_int),
    ('flags', c_int),
    ('_lambda', real),
    ('box', matrix),
    ('box_rel', matrix),
    ('boxv', matrix),
    ('pres_prev', matrix),
    ('svir_prev', matrix),
    ('fvir_prev', matrix),
    ('nosehoover_xi', POINTER(c_double)),
    ('nosehoover_vxi', POINTER(c_double)),
    ('nhpres_xi', POINTER(c_double)),
    ('nhpres_vxi', POINTER(c_double)),
    ('therm_integral', POINTER(c_double)),
    ('veta', real),
    ('vol0', real),
    ('nalloc', c_int),
    ('x', POINTER(rvec)),
    ('v', POINTER(rvec)),
    ('sd_X', POINTER(rvec)),
    ('cg_p', POINTER(rvec)),
    ('ld_rng', POINTER(c_uint)),
    ('ld_rngi', POINTER(c_int)),
    ('hist', history_t),
    ('ekinstate', ekinstate_t),
    ('enerhist', energyhistory_t),
    ('ddp_count', c_int),
    ('ddp_count_cg_gl', c_int),
    ('ncg_gl', c_int),
    ('cg_gl', POINTER(c_int)),
    ('cg_gl_nalloc', c_int),
]

t_state = struct_anon_250 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 174

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 182
class struct_anon_251(Structure):
    pass

struct_anon_251.__slots__ = [
    'Qinv',
    'QPinv',
    'Winv',
    'Winvm',
]
struct_anon_251._fields_ = [
    ('Qinv', POINTER(c_double)),
    ('QPinv', POINTER(c_double)),
    ('Winv', c_double),
    ('Winvm', tensor),
]

t_extmass = struct_anon_251 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 182

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 193
class struct_anon_252(Structure):
    pass

struct_anon_252.__slots__ = [
    'veta',
    'rscale',
    'vscale',
    'rvscale',
    'alpha',
    'vscale_nhc',
]
struct_anon_252._fields_ = [
    ('veta', real),
    ('rscale', c_double),
    ('vscale', c_double),
    ('rvscale', c_double),
    ('alpha', c_double),
    ('vscale_nhc', POINTER(c_double)),
]

t_vetavars = struct_anon_252 # /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 193

# /home/piton/scr/gromacs-4.5.5/include/types/../types/shellfc.h: 45
class struct_gmx_shellfc(Structure):
    pass

gmx_shellfc_t = POINTER(struct_gmx_shellfc) # /home/piton/scr/gromacs-4.5.5/include/types/../types/shellfc.h: 45

# /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 44
class struct_anon_253(Structure):
    pass

struct_anon_253.__slots__ = [
    'r',
    'g',
    'b',
]
struct_anon_253._fields_ = [
    ('r', real),
    ('g', real),
    ('b', real),
]

t_rgb = struct_anon_253 # /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 44

# /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 52
class struct_anon_254(Structure):
    pass

struct_anon_254.__slots__ = [
    'c1',
    'c2',
]
struct_anon_254._fields_ = [
    ('c1', c_char),
    ('c2', c_char),
]

t_xpmelmt = struct_anon_254 # /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 52

t_matelmt = c_short # /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 54

# /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 60
class struct_anon_255(Structure):
    pass

struct_anon_255.__slots__ = [
    'code',
    'desc',
    'rgb',
]
struct_anon_255._fields_ = [
    ('code', t_xpmelmt),
    ('desc', String),
    ('rgb', t_rgb),
]

t_mapping = struct_anon_255 # /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 60

# /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 81
for _lib in _libs.values():
    try:
        nmap = (c_int).in_dll(_lib, 'nmap')
        break
    except:
        pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 82
for _lib in _libs.values():
    try:
        map = (POINTER(t_mapping)).in_dll(_lib, 'map')
        break
    except:
        pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/oenv.h: 41
class struct_output_env(Structure):
    pass

output_env_t = POINTER(struct_output_env) # /home/piton/scr/gromacs-4.5.5/include/types/../types/oenv.h: 41

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nlistheuristics.h: 59
class struct_anon_256(Structure):
    pass

struct_anon_256.__slots__ = [
    'bGStatEveryStep',
    'step_ns',
    'step_nscheck',
    'nns',
    'scale_tot',
    'nabnsb',
    's1',
    's2',
    'ab',
    'lt_runav',
    'lt_runav2',
]
struct_anon_256._fields_ = [
    ('bGStatEveryStep', gmx_bool),
    ('step_ns', gmx_large_int_t),
    ('step_nscheck', gmx_large_int_t),
    ('nns', gmx_large_int_t),
    ('scale_tot', matrix),
    ('nabnsb', c_int),
    ('s1', c_double),
    ('s2', c_double),
    ('ab', c_double),
    ('lt_runav', c_double),
    ('lt_runav2', c_double),
]

gmx_nlheur_t = struct_anon_256 # /home/piton/scr/gromacs-4.5.5/include/types/../types/nlistheuristics.h: 59

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nlistheuristics.h: 61
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'reset_nlistheuristics'):
        continue
    reset_nlistheuristics = _lib.reset_nlistheuristics
    reset_nlistheuristics.argtypes = [POINTER(gmx_nlheur_t), gmx_large_int_t]
    reset_nlistheuristics.restype = None
    break

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nlistheuristics.h: 63
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_nlistheuristics'):
        continue
    init_nlistheuristics = _lib.init_nlistheuristics
    init_nlistheuristics.argtypes = [POINTER(gmx_nlheur_t), gmx_bool, gmx_large_int_t]
    init_nlistheuristics.restype = None
    break

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nlistheuristics.h: 66
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'update_nliststatistics'):
        continue
    update_nliststatistics = _lib.update_nliststatistics
    update_nliststatistics.argtypes = [POINTER(gmx_nlheur_t), gmx_large_int_t]
    update_nliststatistics.restype = None
    break

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nlistheuristics.h: 68
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'set_nlistheuristics'):
        continue
    set_nlistheuristics = _lib.set_nlistheuristics
    set_nlistheuristics.argtypes = [POINTER(gmx_nlheur_t), gmx_bool, gmx_large_int_t]
    set_nlistheuristics.restype = None
    break

# /home/piton/scr/gromacs-4.5.5/include/types/../types/iteratedconstraints.h: 60
class struct_anon_257(Structure):
    pass

struct_anon_257.__slots__ = [
    'f',
    'fprev',
    'x',
    'xprev',
    'iter_i',
    'bIterate',
    'allrelerr',
    'num_close',
]
struct_anon_257._fields_ = [
    ('f', real),
    ('fprev', real),
    ('x', real),
    ('xprev', real),
    ('iter_i', c_int),
    ('bIterate', gmx_bool),
    ('allrelerr', real * (50 + 2)),
    ('num_close', c_int),
]

gmx_iterate_t = struct_anon_257 # /home/piton/scr/gromacs-4.5.5/include/types/../types/iteratedconstraints.h: 60

# /home/piton/scr/gromacs-4.5.5/include/types/../types/iteratedconstraints.h: 62
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gmx_iterate_init'):
        continue
    gmx_iterate_init = _lib.gmx_iterate_init
    gmx_iterate_init.argtypes = [POINTER(gmx_iterate_t), gmx_bool]
    gmx_iterate_init.restype = None
    break

# /home/piton/scr/gromacs-4.5.5/include/types/../types/iteratedconstraints.h: 64
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'done_iterating'):
        continue
    done_iterating = _lib.done_iterating
    done_iterating.argtypes = [POINTER(t_commrec), POINTER(FILE), c_int, POINTER(gmx_iterate_t), gmx_bool, real, POINTER(real)]
    done_iterating.restype = gmx_bool
    break

t_ifunc = CFUNCTYPE(UNCHECKED(real), c_int, POINTER(t_iatom), POINTER(t_iparams), POINTER(rvec), POINTER(rvec), POINTER(rvec), POINTER(t_pbc), POINTER(t_graph), real, POINTER(real), POINTER(t_mdatoms), POINTER(t_fcdata), POINTER(c_int)) # /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 47

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 101
class struct_anon_258(Structure):
    pass

struct_anon_258.__slots__ = [
    'name',
    'longname',
    'nratoms',
    'nrfpA',
    'nrfpB',
    'flags',
    'nrnb_ind',
    'ifunc',
]
struct_anon_258._fields_ = [
    ('name', String),
    ('longname', String),
    ('nratoms', c_int),
    ('nrfpA', c_int),
    ('nrfpB', c_int),
    ('flags', c_ulong),
    ('nrnb_ind', c_int),
    ('ifunc', POINTER(t_ifunc)),
]

t_interaction_function = struct_anon_258 # /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 101

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 119
for _lib in _libs.values():
    try:
        interaction_function = (t_interaction_function * F_NRE).in_dll(_lib, 'interaction_function')
        break
    except:
        pass

# /home/piton/scr/gromacs-4.5.5/include/types/matrix.h: 81
for _lib in _libs.values():
    try:
        nmap = (c_int).in_dll(_lib, 'nmap')
        break
    except:
        pass

# /home/piton/scr/gromacs-4.5.5/include/types/matrix.h: 82
for _lib in _libs.values():
    try:
        map = (POINTER(t_mapping)).in_dll(_lib, 'map')
        break
    except:
        pass

enum_anon_259 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ = 0 # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDW = (eNL_VDWQQ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ = (eNL_VDW + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ_FREE = (eNL_QQ + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDW_FREE = (eNL_VDWQQ_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ_FREE = (eNL_VDW_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ_WATER = (eNL_QQ_FREE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ_WATER = (eNL_VDWQQ_WATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_VDWQQ_WATERWATER = (eNL_QQ_WATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_QQ_WATERWATER = (eNL_VDWQQ_WATERWATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

eNL_NR = (eNL_QQ_WATERWATER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 42

enum_anon_260 = c_int # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcTC = 0 # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcENER = (egcTC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcACC = (egcENER + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcFREEZE = (egcACC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcUser1 = (egcFREEZE + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcUser2 = (egcUser1 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcVCM = (egcUser2 + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcXTC = (egcVCM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcORFIT = (egcXTC + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcQMMM = (egcORFIT + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

egcNR = (egcQMMM + 1) # /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 46

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 63
try:
    XX = 0
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 64
try:
    YY = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 65
try:
    ZZ = 2
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 66
try:
    DIM = 3
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 67
try:
    XXXX = 0
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 68
try:
    XXYY = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 69
try:
    XXZZ = 2
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 70
try:
    YYXX = 3
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 71
try:
    YYYY = 4
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 72
try:
    YYZZ = 5
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 73
try:
    ZZXX = 6
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 74
try:
    ZZYY = 7
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 75
try:
    ZZZZ = 8
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 88
try:
    FALSE = 0
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 91
try:
    TRUE = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 93
try:
    BOOL_NR = 2
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 97
try:
    NO_ATID = (~0)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 100
try:
    GMX_DOUBLE_EPS = 1.11022302e-16
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 103
try:
    GMX_DOUBLE_MAX = 1.79769312e+308
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 106
try:
    GMX_DOUBLE_MIN = 2.22507386e-308
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 109
try:
    GMX_FLOAT_EPS = 5.96046448e-08
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 112
try:
    GMX_FLOAT_MAX = 3.40282346e+38
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 115
try:
    GMX_FLOAT_MIN = 1.17549435e-38
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 139
try:
    GMX_REAL_EPS = GMX_FLOAT_EPS
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 140
try:
    GMX_REAL_MIN = GMX_FLOAT_MIN
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 141
try:
    GMX_REAL_MAX = GMX_FLOAT_MAX
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 142
try:
    gmx_real_fullprecision_pfmt = '%14.7e'
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 173
try:
    gmx_large_int_fmt = 'lld'
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 174
try:
    gmx_large_int_pfmt = '%lld'
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 175
try:
    SIZEOF_GMX_LARGE_INT = 8
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 176
try:
    GMX_LARGE_INT_MAX = 9223372036854775807L
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/simple.h: 177
try:
    GMX_LARGE_INT_MIN = ((-GMX_LARGE_INT_MAX) - 1L)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/atoms.h: 113
def PERTURBED(a):
    return (((((a.mB).value) != ((a.m).value)) or (((a.qB).value) != ((a.q).value))) or (((a.typeB).value) != ((a.type).value)))

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 48
try:
    MAXATOMLIST = 6
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 49
try:
    MAXFORCEPARAM = 12
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 50
try:
    NR_RBDIHS = 6
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/idef.h: 51
try:
    NR_FOURDIHS = 4
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 58
try:
    DD_MAXZONE = 8
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 59
try:
    DD_MAXIZONE = 4
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 235
try:
    DUTY_PP = (1 << 0)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 236
try:
    DUTY_PME = (1 << 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 286
def MASTERNODE(cr):
    return (((cr.contents.nodeid).value) == 0)

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 289
def MASTER(cr):
    return (MASTERNODE (cr))

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 290
def SIMMASTER(cr):
    return ((MASTER (cr)) and (((cr.contents.duty).value) & DUTY_PP))

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 291
def NODEPAR(cr):
    return (((cr.contents.nnodes).value) > 1)

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 294
def PAR(cr):
    return (NODEPAR (cr))

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 295
def RANK(cr, nodeid):
    return nodeid

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 296
def MASTERRANK(cr):
    return 0

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 298
def DOMAINDECOMP(cr):
    return (((cr.contents.dd).value) != NULL)

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 299
def DDMASTER(dd):
    return (((dd.contents.rank).value) == ((dd.contents.masterrank).value))

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 301
def PARTDECOMP(cr):
    return (((cr.contents.pd).value) != NULL)

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 303
def MULTISIM(cr):
    return (cr.contents.ms)

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 304
def MSRANK(ms, nodeid):
    return nodeid

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 305
def MASTERSIM(ms):
    return (((ms.contents.sim).value) == 0)

# /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 308
def MULTIMASTER(cr):
    return ((SIMMASTER (cr)) and ((not (MULTISIM (cr))) or (MASTERSIM ((cr.contents.ms)))))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 90
def EEL_RF(e):
    return ((((e == eelRF) or (e == eelGRF)) or (e == eelRF_NEC)) or (e == eelRF_ZERO))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 92
def EEL_PME(e):
    return ((((e == eelPME) or (e == eelPMESWITCH)) or (e == eelPMEUSER)) or (e == eelPMEUSERSWITCH))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 93
def EEL_FULL(e):
    return ((((EEL_PME (e)) or (e == eelPPPM)) or (e == eelPOISSON)) or (e == eelEWALD))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 95
def EEL_SWITCHED(e):
    return (((((e == eelSWITCH) or (e == eelSHIFT)) or (e == eelENCADSHIFT)) or (e == eelPMESWITCH)) or (e == eelPMEUSERSWITCH))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 97
def EEL_IS_ZERO_AT_CUTOFF(e):
    return ((EEL_SWITCHED (e)) or (e == eelRF_ZERO))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 99
def EEL_MIGHT_BE_ZERO_AT_CUTOFF(e):
    return (((EEL_IS_ZERO_AT_CUTOFF (e)) or (e == eelUSER)) or (e == eelPMEUSER))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 105
def EVDW_SWITCHED(e):
    return (((e == evdwSWITCH) or (e == evdwSHIFT)) or (e == evdwENCADSHIFT))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 107
def EVDW_IS_ZERO_AT_CUTOFF(e):
    return (EVDW_SWITCHED (e))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 109
def EVDW_MIGHT_BE_ZERO_AT_CUTOFF(e):
    return ((EVDW_IS_ZERO_AT_CUTOFF (e)) or (e == evdwUSER))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 121
def EI_VV(e):
    return ((e == eiVV) or (e == eiVVAK))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 122
def EI_SD(e):
    return ((e == eiSD1) or (e == eiSD2))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 123
def EI_RANDOM(e):
    return ((EI_SD (e)) or (e == eiBD))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 125
def EI_DYNAMICS(e):
    return ((((e == eiMD) or (EI_SD (e))) or (e == eiBD)) or (EI_VV (e)))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 126
def EI_ENERGY_MINIMIZATION(e):
    return (((e == eiSteep) or (e == eiCG)) or (e == eiLBFGS))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 127
def EI_TPI(e):
    return ((e == eiTPI) or (e == eiTPIC))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 129
def EI_STATE_VELOCITY(e):
    return (((e == eiMD) or (EI_VV (e))) or (EI_SD (e)))

# /home/piton/scr/gromacs-4.5.5/include/types/enums.h: 225
def PULL_CYL(pull):
    return (((pull.contents.eGeom).value) == epullgCYL)

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 73
try:
    ffSET = (1 << 0)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 74
try:
    ffREAD = (1 << 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 75
try:
    ffWRITE = (1 << 2)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 76
try:
    ffOPT = (1 << 3)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 77
try:
    ffLIB = (1 << 4)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 78
try:
    ffMULT = (1 << 5)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 79
try:
    ffRW = (ffREAD | ffWRITE)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 80
try:
    ffOPTRD = (ffREAD | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 81
try:
    ffOPTWR = (ffWRITE | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 82
try:
    ffOPTRW = (ffRW | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 83
try:
    ffLIBRD = (ffREAD | ffLIB)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 84
try:
    ffLIBOPTRD = (ffOPTRD | ffLIB)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 85
try:
    ffRDMULT = (ffREAD | ffMULT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 86
try:
    ffOPTRDMULT = (ffRDMULT | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 87
try:
    ffWRMULT = (ffWRITE | ffMULT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/filenm.h: 88
try:
    ffOPTWRMULT = (ffWRMULT | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 56
try:
    MAX_CHARGEGROUP_SIZE = 32
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/nblist.h: 61
try:
    MAX_CGCGSIZE = 32
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 48
try:
    MAX_CG = 1024
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 78
def GET_CGINFO_GID(cgi):
    return (cgi & 65535)

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 80
def GET_CGINFO_EXCL_INTRA(cgi):
    return (cgi & (1 << 16))

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 82
def GET_CGINFO_EXCL_INTER(cgi):
    return (cgi & (1 << 17))

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 84
def GET_CGINFO_SOLOPT(cgi):
    return ((cgi >> 18) & 15)

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 87
def GET_CGINFO_BOND_INTER(cgi):
    return (cgi & (1 << 22))

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 89
def GET_CGINFO_NATOMS(cgi):
    return ((cgi >> 23) & 255)

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 96
try:
    GMX_CUTOFF_INF = 1e+18
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 371
def C6(nbfp, ntp, ai, aj):
    return (nbfp [(2 * ((ntp * ai) + aj))])

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 372
def C12(nbfp, ntp, ai, aj):
    return (nbfp [((2 * ((ntp * ai) + aj)) + 1)])

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 373
def BHAMC(nbfp, ntp, ai, aj):
    return (nbfp [(3 * ((ntp * ai) + aj))])

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 374
def BHAMA(nbfp, ntp, ai, aj):
    return (nbfp [((3 * ((ntp * ai) + aj)) + 1)])

# /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 375
def BHAMB(nbfp, ntp, ai, aj):
    return (nbfp [((3 * ((ntp * ai) + aj)) + 2)])

# /home/piton/scr/gromacs-4.5.5/include/types/graph.h: 59
def SHIFT_IVEC(g, i):
    return ((g.contents.ishift) [(i - ((g.contents.start).value))])

# /home/piton/scr/gromacs-4.5.5/include/types/group.h: 83
def GID(igid, jgid, gnr):
    return (igid < jgid) and ((igid * gnr) + jgid) or ((jgid * gnr) + igid)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 90
def EEL_RF(e):
    return ((((e == eelRF) or (e == eelGRF)) or (e == eelRF_NEC)) or (e == eelRF_ZERO))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 92
def EEL_PME(e):
    return ((((e == eelPME) or (e == eelPMESWITCH)) or (e == eelPMEUSER)) or (e == eelPMEUSERSWITCH))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 93
def EEL_FULL(e):
    return ((((EEL_PME (e)) or (e == eelPPPM)) or (e == eelPOISSON)) or (e == eelEWALD))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 95
def EEL_SWITCHED(e):
    return (((((e == eelSWITCH) or (e == eelSHIFT)) or (e == eelENCADSHIFT)) or (e == eelPMESWITCH)) or (e == eelPMEUSERSWITCH))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 97
def EEL_IS_ZERO_AT_CUTOFF(e):
    return ((EEL_SWITCHED (e)) or (e == eelRF_ZERO))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 99
def EEL_MIGHT_BE_ZERO_AT_CUTOFF(e):
    return (((EEL_IS_ZERO_AT_CUTOFF (e)) or (e == eelUSER)) or (e == eelPMEUSER))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 105
def EVDW_SWITCHED(e):
    return (((e == evdwSWITCH) or (e == evdwSHIFT)) or (e == evdwENCADSHIFT))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 107
def EVDW_IS_ZERO_AT_CUTOFF(e):
    return (EVDW_SWITCHED (e))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 109
def EVDW_MIGHT_BE_ZERO_AT_CUTOFF(e):
    return ((EVDW_IS_ZERO_AT_CUTOFF (e)) or (e == evdwUSER))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 121
def EI_VV(e):
    return ((e == eiVV) or (e == eiVVAK))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 122
def EI_SD(e):
    return ((e == eiSD1) or (e == eiSD2))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 123
def EI_RANDOM(e):
    return ((EI_SD (e)) or (e == eiBD))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 125
def EI_DYNAMICS(e):
    return ((((e == eiMD) or (EI_SD (e))) or (e == eiBD)) or (EI_VV (e)))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 126
def EI_ENERGY_MINIMIZATION(e):
    return (((e == eiSteep) or (e == eiCG)) or (e == eiLBFGS))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 127
def EI_TPI(e):
    return ((e == eiTPI) or (e == eiTPIC))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 129
def EI_STATE_VELOCITY(e):
    return (((e == eiMD) or (EI_VV (e))) or (EI_SD (e)))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/enums.h: 225
def PULL_CYL(pull):
    return (((pull.contents.eGeom).value) == epullgCYL)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/topology.h: 83
def ggrpnr(groups, egc, i):
    return ((groups.contents.grpnr) [egc]) and (((groups.contents.grpnr) [egc]) [i]) or 0

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 60
try:
    EGP_EXCL = (1 << 0)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 61
try:
    EGP_TABLE = (1 << 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 289
def DEFORM(ir):
    return ((((((((((ir.deform).value) [XX]) [XX]) != 0) or (((((ir.deform).value) [YY]) [YY]) != 0)) or (((((ir.deform).value) [ZZ]) [ZZ]) != 0)) or (((((ir.deform).value) [YY]) [XX]) != 0)) or (((((ir.deform).value) [ZZ]) [XX]) != 0)) or (((((ir.deform).value) [ZZ]) [YY]) != 0))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 291
def DYNAMIC_BOX(ir):
    return (((((ir.epc).value) != epcNO) or (((ir.eI).value) == eiTPI)) or (DEFORM (ir)))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 293
def PRESERVE_SHAPE(ir):
    return (((((ir.epc).value) != epcNO) and (((((ir.deform).value) [XX]) [XX]) == 0)) and ((((ir.epct).value) == epctISOTROPIC) or (((ir.epct).value) == epctSEMIISOTROPIC)))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 295
def NEED_MUTOT(ir):
    return (((((ir.coulombtype).value) == eelEWALD) or (EEL_PME ((ir.coulombtype)))) and ((((ir.ewald_geometry).value) == eewg3DC) or (((ir.epsilon_surface).value) != 0)))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 297
def IR_TWINRANGE(ir):
    return ((((ir.rlist).value) > 0) and ((((ir.rlistlong).value) == 0) or (((ir.rlistlong).value) > ((ir.rlist).value))))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 299
def IR_ELEC_FIELD(ir):
    return ((((((((ir.ex).value) [XX]).n).value) > 0) or ((((((ir.ex).value) [YY]).n).value) > 0)) or ((((((ir.ex).value) [ZZ]).n).value) > 0))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 301
def IR_EXCL_FORCES(ir):
    return (((EEL_FULL ((ir.coulombtype))) or ((EEL_RF ((ir.coulombtype))) and (((ir.coulombtype).value) != eelRF_NEC))) or (((ir.implicit_solvent).value) != eisNO))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 303
def IR_NVT_TROTTER(ir):
    return (((((ir.contents.eI).value) == eiVV) or (((ir.contents.eI).value) == eiVVAK)) and (((ir.contents.etc).value) == etcNOSEHOOVER))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/inputrec.h: 305
def IR_NPT_TROTTER(ir):
    return (((((ir.contents.eI).value) == eiVV) or (((ir.contents.eI).value) == eiVVAK)) and (((ir.contents.epc).value) == epcMTTK))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 43
try:
    D_BOX_Z = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 44
try:
    D_BOX_Y = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 45
try:
    D_BOX_X = 2
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 46
try:
    N_BOX_Z = ((2 * D_BOX_Z) + 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 47
try:
    N_BOX_Y = ((2 * D_BOX_Y) + 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 48
try:
    N_BOX_X = ((2 * D_BOX_X) + 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 49
try:
    N_IVEC = ((N_BOX_Z * N_BOX_Y) * N_BOX_X)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 50
try:
    CENTRAL = (N_IVEC / 2)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 51
try:
    SHIFTS = N_IVEC
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 53
def XYZ2IS(x, y, z):
    return (((N_BOX_X * (((N_BOX_Y * (z + D_BOX_Z)) + y) + D_BOX_Y)) + x) + D_BOX_X)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 54
def IVEC2IS(iv):
    return (XYZ2IS ((iv [XX]), (iv [YY]), (iv [ZZ])))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 55
def IS2X(iv):
    return ((iv % N_BOX_X) - D_BOX_X)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 56
def IS2Y(iv):
    return (((iv / N_BOX_X) % N_BOX_Y) - D_BOX_Y)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ishift.h: 57
def IS2Z(iv):
    return ((iv / (N_BOX_X * N_BOX_Y)) - D_BOX_Z)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/graph.h: 59
def SHIFT_IVEC(g, i):
    return ((g.contents.ishift) [(i - ((g.contents.start).value))])

# /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 56
try:
    eNR_NBKERNEL_NONE = (-1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/ns.h: 48
try:
    MAX_CG = 1024
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 78
def GET_CGINFO_GID(cgi):
    return (cgi & 65535)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 80
def GET_CGINFO_EXCL_INTRA(cgi):
    return (cgi & (1 << 16))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 82
def GET_CGINFO_EXCL_INTER(cgi):
    return (cgi & (1 << 17))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 84
def GET_CGINFO_SOLOPT(cgi):
    return ((cgi >> 18) & 15)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 87
def GET_CGINFO_BOND_INTER(cgi):
    return (cgi & (1 << 22))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 89
def GET_CGINFO_NATOMS(cgi):
    return ((cgi >> 23) & 255)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 96
try:
    GMX_CUTOFF_INF = 1e+18
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 371
def C6(nbfp, ntp, ai, aj):
    return (nbfp [(2 * ((ntp * ai) + aj))])

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 372
def C12(nbfp, ntp, ai, aj):
    return (nbfp [((2 * ((ntp * ai) + aj)) + 1)])

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 373
def BHAMC(nbfp, ntp, ai, aj):
    return (nbfp [(3 * ((ntp * ai) + aj))])

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 374
def BHAMA(nbfp, ntp, ai, aj):
    return (nbfp [((3 * ((ntp * ai) + aj)) + 1)])

# /home/piton/scr/gromacs-4.5.5/include/types/../types/forcerec.h: 375
def BHAMB(nbfp, ntp, ai, aj):
    return (nbfp [((3 * ((ntp * ai) + aj)) + 2)])

# /home/piton/scr/gromacs-4.5.5/include/types/../types/pbc.h: 49
try:
    MAX_NTRICVEC = 12
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 73
try:
    ffSET = (1 << 0)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 74
try:
    ffREAD = (1 << 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 75
try:
    ffWRITE = (1 << 2)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 76
try:
    ffOPT = (1 << 3)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 77
try:
    ffLIB = (1 << 4)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 78
try:
    ffMULT = (1 << 5)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 79
try:
    ffRW = (ffREAD | ffWRITE)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 80
try:
    ffOPTRD = (ffREAD | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 81
try:
    ffOPTWR = (ffWRITE | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 82
try:
    ffOPTRW = (ffRW | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 83
try:
    ffLIBRD = (ffREAD | ffLIB)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 84
try:
    ffLIBOPTRD = (ffOPTRD | ffLIB)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 85
try:
    ffRDMULT = (ffREAD | ffMULT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 86
try:
    ffOPTRDMULT = (ffRDMULT | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 87
try:
    ffWRMULT = (ffWRITE | ffMULT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/filenm.h: 88
try:
    ffOPTWRMULT = (ffWRMULT | ffOPT)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/group.h: 83
def GID(igid, jgid, gnr):
    return (igid < jgid) and ((igid * gnr) + jgid) or ((jgid * gnr) + igid)

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 52
try:
    NHCHAINLENGTH = 10
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/state.h: 66
def EST_DISTR(e):
    return (not (((e >= estLAMBDA) and (e <= estTC_INT)) or ((e >= estSVIR_PREV) and (e <= estFVIR_PREV))))

# /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 62
try:
    MAT_SPATIAL_X = (1 << 0)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/matrix.h: 63
try:
    MAT_SPATIAL_Y = (1 << 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/../types/iteratedconstraints.h: 50
try:
    MAXITERCONST = 50
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 69
try:
    IF_NULL = 0
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 70
try:
    IF_BOND = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 71
try:
    IF_VSITE = (1 << 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 72
try:
    IF_CONSTRAINT = (1 << 2)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 73
try:
    IF_CHEMBOND = (1 << 3)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 74
try:
    IF_BTYPE = (1 << 4)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 75
try:
    IF_ATYPE = (1 << 5)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 76
try:
    IF_TABULATED = (1 << 6)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 77
try:
    IF_LIMZERO = (1 << 7)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 103
def NRFPA(ftype):
    return ((interaction_function [ftype]).nrfpA)

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 104
def NRFPB(ftype):
    return ((interaction_function [ftype]).nrfpB)

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 105
def NRFP(ftype):
    return (((NRFPA (ftype)).value) + ((NRFPB (ftype)).value))

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 106
def NRAL(ftype):
    return ((interaction_function [ftype]).nratoms)

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 108
def IS_CHEMBOND(ftype):
    return (((((interaction_function [ftype]).nratoms).value) == 2) and ((((interaction_function [ftype]).flags).value) & IF_CHEMBOND))

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 114
def IS_ANGLE(ftype):
    return (((((interaction_function [ftype]).nratoms).value) == 3) and ((((interaction_function [ftype]).flags).value) & IF_ATYPE))

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 115
def IS_VSITE(ftype):
    return ((((interaction_function [ftype]).flags).value) & IF_VSITE)

# /home/piton/scr/gromacs-4.5.5/include/types/ifunc.h: 117
def IS_TABULATED(ftype):
    return ((((interaction_function [ftype]).flags).value) & IF_TABULATED)

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 43
try:
    D_BOX_Z = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 44
try:
    D_BOX_Y = 1
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 45
try:
    D_BOX_X = 2
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 46
try:
    N_BOX_Z = ((2 * D_BOX_Z) + 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 47
try:
    N_BOX_Y = ((2 * D_BOX_Y) + 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 48
try:
    N_BOX_X = ((2 * D_BOX_X) + 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 49
try:
    N_IVEC = ((N_BOX_Z * N_BOX_Y) * N_BOX_X)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 50
try:
    CENTRAL = (N_IVEC / 2)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 51
try:
    SHIFTS = N_IVEC
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 53
def XYZ2IS(x, y, z):
    return (((N_BOX_X * (((N_BOX_Y * (z + D_BOX_Z)) + y) + D_BOX_Y)) + x) + D_BOX_X)

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 54
def IVEC2IS(iv):
    return (XYZ2IS ((iv [XX]), (iv [YY]), (iv [ZZ])))

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 55
def IS2X(iv):
    return ((iv % N_BOX_X) - D_BOX_X)

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 56
def IS2Y(iv):
    return (((iv / N_BOX_X) % N_BOX_Y) - D_BOX_Y)

# /home/piton/scr/gromacs-4.5.5/include/types/ishift.h: 57
def IS2Z(iv):
    return ((iv / (N_BOX_X * N_BOX_Y)) - D_BOX_Z)

# /home/piton/scr/gromacs-4.5.5/include/types/matrix.h: 62
try:
    MAT_SPATIAL_X = (1 << 0)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/matrix.h: 63
try:
    MAT_SPATIAL_Y = (1 << 1)
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/ns.h: 48
try:
    MAX_CG = 1024
except:
    pass

# /home/piton/scr/gromacs-4.5.5/include/types/topology.h: 83
def ggrpnr(groups, egc, i):
    return ((groups.contents.grpnr) [egc]) and (((groups.contents.grpnr) [egc]) [i]) or 0

gmx_domdec_master = struct_gmx_domdec_master # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 61

gmx_ga2la = struct_gmx_ga2la # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 86

gmx_reverse_top = struct_gmx_reverse_top # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 88

gmx_domdec_constraints = struct_gmx_domdec_constraints # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 90

gmx_domdec_specat_comm = struct_gmx_domdec_specat_comm # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 92

gmx_domdec_comm = struct_gmx_domdec_comm # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 94

gmx_pme_comm_n_box = struct_gmx_pme_comm_n_box # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 96

gmx_partdec = struct_gmx_partdec # /home/piton/scr/gromacs-4.5.5/include/types/commrec.h: 223

gmx_lincsdata = struct_gmx_lincsdata # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 44

gmx_shakedata = struct_gmx_shakedata # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 47

gmx_settledata = struct_gmx_settledata # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 50

gmx_constr = struct_gmx_constr # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 53

gmx_edsam = struct_gmx_edsam # /home/piton/scr/gromacs-4.5.5/include/types/constr.h: 56

gbtmpnbls = struct_gbtmpnbls # /home/piton/scr/gromacs-4.5.5/include/types/genborn.h: 50

gmx_pme = struct_gmx_pme # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 46

ewald_tab = struct_ewald_tab # /home/piton/scr/gromacs-4.5.5/include/types/forcerec.h: 130

symbuf = struct_symbuf # /home/piton/scr/gromacs-4.5.5/include/types/../types/symtab.h: 43

trxframe = struct_trxframe # /home/piton/scr/gromacs-4.5.5/include/types/../types/trx.h: 49

gmx_wallcycle = struct_gmx_wallcycle # /home/piton/scr/gromacs-4.5.5/include/types/../types/nrnb.h: 128

gmx_shellfc = struct_gmx_shellfc # /home/piton/scr/gromacs-4.5.5/include/types/../types/shellfc.h: 45

output_env = struct_output_env # /home/piton/scr/gromacs-4.5.5/include/types/../types/oenv.h: 41

# No inserted files

