import contextlib
import functools
import importlib
import logging
import os
import pkgutil
import re
import sys

import time
from io import StringIO
# from itertools import cycle
# from dtk import __version__ as DTK_VERSION

# logging_initialized = False

# animation = cycle(("\u25f0", "\u25f1", "\u25f2", "\u25f3",))
# animation = cycle(("|", "/", "-", "\\"))


# def init_logging(name):
#     import logging.config
#     global logging_initialized
#
#     if not logging_initialized:
#         current_dir = os.path.dirname(os.path.realpath(__file__))
#         logging.config.fileConfig(os.path.join(current_dir, 'logging.ini'), disable_existing_loggers=False)
#         logging_initialized = True
#     return logging.getLogger(name)
#
#
# try:
#     logger = init_logging('Utils')
# except:
#     pass
#
#
# def retrieve_item(itemid):
#     """
#     Return the object identified by id.
#     Can be an experiment, a suite or a batch.
#     If it is a suite, all experiments with this suite_id will be returned.
#     """
#     # First try to get an experiment
#     from simtools.Utilities.Experiments import retrieve_experiment
#     from simtools.DataAccess.DataStore import DataStore
#     from simtools.Utilities.COMPSUtilities import exps_for_suite_id
#     from simtools.Utilities.Experiments import retrieve_simulation
#
#     # Try experiments first
#     try:
#         return retrieve_experiment(itemid)
#     except:
#         pass
#
#     # This was not an experiment, maybe a batch ?
#     batch = DataStore.get_batch_by_id(itemid)
#     if batch: return batch
#
#     batch = DataStore.get_batch_by_name(itemid)
#     if batch: return batch
#
#     # Still no item found -> test the suites
#     exps = DataStore.get_experiments_by_suite(itemid)
#     if exps: return exps
#
#     # Still no item found -> test the simulations
#     sim = DataStore.get_simulation(itemid)
#     if sim: return sim
#
#     # Still not -> last chance is a COMPS suite
#     exps = exps_for_suite_id(itemid)
#     if exps: return [retrieve_experiment(str(exp.id)) for exp in exps]
#
#     # Nothing, consider COMPS simulation
#     try:
#         return retrieve_simulation(itemid)
#     except:
#         pass
#
#     # Didnt find anything sorry
#     raise (Exception('Could not find any item corresponding to %s' % itemid))
#
#
# def utc_to_local(utc_dt):
#     import pytz
#     from pytz import timezone
#
#     local_tz = timezone('US/Pacific')
#     local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
#     return local_tz.normalize(local_dt)  # .normalize might be unnecessary
#
#
# @contextlib.contextmanager
# def nostdout(stdout=False, stderr=False):
#     """
#     Context used to suppress any print/logging from block of code
#
#     Args:
#         stdout: If False, hides. If True Shows. False by default
#         stderr: If False, hides. If True Shows. False by default
#     """
#     # Save current state and disable output
#     if not stdout:
#         save_stdout = sys.stdout
#         sys.stdout = StringIO()
#     if not stderr:
#         save_stderr = sys.stderr
#         sys.stderr = StringIO()
#
#     # Deactivate logging
#     previous_level = logging.root.manager.disable
#     logging.disable(logging.ERROR)
#
#     yield
#
#     # Restore
#     if not stdout:
#         sys.stdout = save_stdout
#     if not stderr:
#         sys.stderr = save_stderr
#
#     logging.disable(previous_level)
#
#
# def retry_function(func, wait=1.5, max_retries=5):
#     """
#     Decorator allowing to retry the call to a function with some time in between.
#     Usage::
#
#         @retry_function
#         def my_func():
#             pass
#
#         @retry_function(max_retries=10, wait=2)
#         def my_func():
#             pass
#
#     :param func:
#     :param time_between_tries:
#     :param max_retries:
#
#     :return:
#     """
#
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         retExc = None
#         for i in range(max_retries):
#             try:
#                 return func(*args, **kwargs)
#             except RuntimeError as r:
#                 # Immediately raise if this is an error.
#                 # COMPS is reachable so let's be clever and trust COMPS
#                 if str(r) == "404 NotFound - Failed to retrieve experiment for given id":
#                     raise r
#             except Exception as e:
#                 retExc = e
#                 time.sleep(wait)
#         raise retExc if retExc else Exception()
#
#     return wrapper
#
#
# def caller_name(skip=2):
#     """
#     Get a name of a caller in the format module.class.method
#
#     `skip` specifies how many levels of stack to skip while getting caller
#     name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.
#
#     An empty string is returned if skipped levels exceed stack height
#     """
#     import inspect
#     stack = inspect.stack()
#     start = 0 + skip
#     if len(stack) < start + 1:
#         return ''
#     parentframe = stack[start][0]
#
#     name = []
#     module = inspect.getmodule(parentframe)
#     # `modname` can be None when frame is executed directly in console
#     if module:
#         name.append(module.__name__)
#     # detect classname
#     if 'self' in parentframe.f_locals:
#         name.append(parentframe.f_locals['self'].__class__.__name__)
#     codename = parentframe.f_code.co_name
#     if codename != '<module>':  # top level usually
#         name.append(codename)  # function or a method
#     del parentframe
#     return ".".join(name)
#
#
# def remove_null_values(null_dict):
#     ret = {}
#     for key, value in null_dict.items():
#         if value:
#             ret[key] = value
#     return ret
#
#
# # def get_tools_revision():
# #     # Get the tools revision
# #     return DTK_VERSION
#
#
# def get_md5(filename):
#     from hashlib import md5
#     import uuid
#     logger.info('Getting md5 for ' + filename)
#
#     if not os.path.exists(filename):
#         logger.error("The file %s does not exist ! No MD5 could be computed..." % filename)
#         return None
#
#     with open(filename, 'rb') as f:
#         md5calc = md5()
#         while True:
#             data = f.read(int(1e8))
#             if len(data) == 0: break
#             md5calc.update(data)
#
#     return uuid.UUID(md5calc.hexdigest())
#
#
# class CommandlineGenerator:
#     """
#     A class to construct command line strings from executable, options, and params
#     """
#
#     def __init__(self, exe_path=None, options=None, params=None):
#         self._exe_path = exe_path
#         self._options = options or {}
#         self._params = [str(p) for p in params] if params else []
#
#     @property
#     def Executable(self):
#         return self._exe_path
#
#     @property
#     def Options(self):
#         options = []
#         for k, v in self._options.items():
#             # Handles spaces
#             value = '"%s"' % v if ' ' in str(v) else str(v)
#             if k[-1] == ':':
#                 options.append(k + value)  # if the option ends in ':', don't insert a space
#             else:
#                 options.extend([k, value])  # otherwise let join (below) add a space
#
#         return ' '.join(options)
#
#     @property
#     def Params(self):
#         return ' '.join(self._params)
#
#     @property
#     def Commandline(self):
#         return ' '.join(filter(None, [self.Executable, self.Options, self.Params]))  # join ignores empty strings
#
#
# def rmtree_f(dir):
#     import shutil
#     if os.path.exists(dir):
#         shutil.rmtree(dir, onerror=rmtree_f_on_error)
#
#
# def rmtree_f_on_error(func, path, exc_info):
#     """
#     Error handler for ``shutil.rmtree``.
#
#     If the error is due to an access error (read only file)
#     it attempts to add write permission and then retries.
#
#     If the error is for another reason it re-raises the error.
#
#     Usage : ``shutil.rmtree(path, onerror=onerror)``
#     """
#     import stat
#     if not os.access(path, os.W_OK):
#         # Is the error an access error ?
#         os.chmod(path, stat.S_IWUSR)
#         func(path)
#     else:
#         raise NameError('os.access error!')
#
#
# def is_running(pid, name_part):
#     """
#     Determines if the given pid is running and is running the specified process (name).
#     :param pid: The pid to check.
#     :param name_part: a case-sensitive partial name by which the thread can be properly identified.
#     :return: True/False
#     """
#     import psutil
#     from simtools.Utilities.LocalOS import LocalOS
#
#     # ck4, This should be refactored to use a common module containing a dict of Process objects
#     #      This way, we don't need to do the name() checking, just use the method process.is_running(),
#     #      since this method checks for pid number being active AND pid start time.
#     if not pid:
#         logger.debug("is_running: no valid pid provided.")
#         return False
#
#     pid = int(pid)
#
#     try:
#         process = psutil.Process(pid)
#     except psutil.NoSuchProcess:
#         logger.debug("is_running: No such process with pid: %d" % pid)
#         return False
#
#     # Retrieve info on the process
#     running = process.is_running()
#     zombie = process.status() == "zombie" if LocalOS.name != LocalOS.WINDOWS else False
#     process_name = process.name()
#     valid_name = name_part.lower() in process_name.lower()
#
#     logger.debug("is_running: pid %s running? %s valid_name (%s)? %s. name: %s" %
#                  (pid, running, name_part, valid_name, process_name))
#
#     if is_running and not zombie and valid_name:
#         logger.debug("is_running: pid %s is running and process name is valid." % pid)
#         return True
#
#     return False
#
#
#
#
# def import_submodules(package, recursive=True):
#     """ Import all submodules of a module, recursively, including subpackages
#
#     :param package: package (name or actual module)
#     :type package: str | module
#     :rtype: dict[str, types.ModuleType]
#     """
#     if isinstance(package, str):
#         package = importlib.import_module(package)
#     results = {}
#     for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
#         full_name = package.__name__ + '.' + name
#         results[full_name] = importlib.import_module(full_name)
#         if recursive and is_pkg:
#             results.update(import_submodules(full_name))
#     return results
#
#
# labels = [
#     (1024 ** 5, ' PB'),
#     (1024 ** 4, ' TB'),
#     (1024 ** 3, ' GB'),
#     (1024 ** 2, ' MB'),
#     (1024 ** 1, ' KB'),
#     (1024 ** 0, (' byte', ' bytes')),
# ]
#
# verbose = [
#     (1024 ** 5, (' petabyte', ' petabytes')),
#     (1024 ** 4, (' terabyte', ' terabytes')),
#     (1024 ** 3, (' gigabyte', ' gigabytes')),
#     (1024 ** 2, (' megabyte', ' megabytes')),
#     (1024 ** 1, (' kilobyte', ' kilobytes')),
#     (1024 ** 0, (' byte', ' bytes')),
# ]
#
#
# def file_size(bytes, system=labels):
#     """
#     Human-readable file size.
#
#     """
#     for factor, suffix in system:
#         if bytes >= factor:
#             break
#     amount = round(bytes / factor)
#     if isinstance(suffix, tuple):
#         singular, multiple = suffix
#         if amount == 1:
#             suffix = singular
#         else:
#             suffix = multiple
#     return str(amount) + suffix
#

def files_in_dir(dir, filters=None):
    """
    Discovers and returns all files in the provided directory matching the provided glob filters. Returned
    paths are relative to the provided directory.
    :param dir: Find files relative to here
    :return: All files discovered as paths relative to dir
    """
    import fnmatch
    import os

    filters = filters or ['*']
    discovered_files = []
    for root, dirnames, filenames in os.walk(dir):
        for filter in filters:
            for filename in fnmatch.filter(filenames, filter):
                trimmed = os.path.join(root, filename).replace("{}{}".format(dir, os.sep), "")
                discovered_files.append(trimmed)
    return discovered_files


# def timestamp(time=None):
#     """
#     :param time: a time object; if None provided, use now.
#     :return: A str timestamp in UTC, format: YYYYMMDD_HHmmSS
#     """
#     import datetime
#     if not time:
#         time = datetime.datetime.utcnow()
#     timestamp = time.strftime('%Y%m%d_%H%M%S')
#     return timestamp
#
#
# def timestamp_filename(filename, time=None):
#     """
#     Create a timestamped filename by appending the time to the given filename.
#     :param filename: any filename to form the prefix of the output filename
#     :return: a filename that is the given filename + a timestamp
#     """
#     new_filename = '.'.join([filename, timestamp(time)])
#     return new_filename
#
#
# def copy_and_reset_StringIO(sio):
#     """
#     A method to copy a StringIO and make sure read access starts at the beginning.
#     :param sio: A StringIO object
#     :return: a copy of sio with read index set to 0
#     """
#     import copy
#     new_sio = copy.deepcopy(sio)
#     new_sio.seek(0)  # just in case the original had been read some
#     return new_sio
#
#
# def batch(iterator, n=1):
#     """
#     Yield n elements from the given iterator at a time
#     :param iterator:
#     :param n:
#     :return:
#     """
#     while True:
#         res = []
#         try:
#             for i in range(n):
#                 res.append(next(iterator))
#         except StopIteration:
#             pass
#         finally:
#             if not res:
#                 raise StopIteration()
#             yield res
#
#
# def batch_list(iterable, n=1):
#     """
#     Batch an iterable passed as argument into lists of n elements.
#
#     Examples:
#         batch([1,2,2,3,4,5,6],2) returns [[1,2],[2,3],[4,5],[6]]
#
#     Args:
#         iterable: The iterable to split
#         n: split in lists of n elements
#
#     Returns: List of lists of n elements
#     """
#     return batch(iter(iterable), n)
#
#
# def remove_special_chars(str, replace="_"):
#     """
#     Removes the special characters from a string and replace them with `replace`.
#
#     Args:
#         str: The string to clean up
#         replace: The character used to replace special
#
#     Returns: Cleaned up string
#     """
#     return re.sub('[^A-Za-z0-9]+', replace, str)
