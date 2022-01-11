from __future__ import annotations
from typing import *

class SBError:
    ...
class SBEvent:
    ...
class SbTypeFormat:
    ...
class SBModule:
    ...
class SBProcess:
    ...
class SBDebugger:
    ...
class CStringStar:
    ...
class SBPlatform:
    ...
class SBSymbolContextList:
    ...
class SBTypeList:
    ...
class BasicType:
    ...
class SBAttachInfo:
    ...
class PIDT:
    ...
class SBListener:
    ...
class SBFileSpec:
    
    ...
class SBSection:
    ...
class MatchType:
    ...
class SBSourceManager:
    ...
class SBBreakpoint:
    ...
class LanguageType:
    ...
class SBEnvironment:
    ...

class SBStructuredData:
    ...
class SBFileSpecList:
    ...
class BreakIdT:
    ...

class SBBreakpointList:
    ...
class SBStringList:
    ...
class WatchIdT:
    ...
class SBBroadcaster:
    ...
class SBInstructionList:
    ...
class DescriptionLevel:
    ...
class SBLaunchInfo:
    ...
class SBTrace:
    ...
class SymbolType:
    ...
class SBBlock:
    ...
class SBFunction:
    ...
class SBCompileUnit:
    ...
class SBLineEntry:
    ...

class SBTarget(object):
    r"""
    Represents the target program running under the debugger.

    SBTarget supports module, breakpoint, and watchpoint iterations. For example, ::

        for m in target.module_iter():
            print m

    produces: ::

        (x86_64) /Volumes/data/lldb/svn/trunk/test/python_api/lldbutil/iter/a.out
        (x86_64) /usr/lib/dyld
        (x86_64) /usr/lib/libstdc++.6.dylib
        (x86_64) /usr/lib/libSystem.B.dylib
        (x86_64) /usr/lib/system/libmathCommon.A.dylib
        (x86_64) /usr/lib/libSystem.B.dylib(__commpage)

    and, ::

        for b in target.breakpoint_iter():
            print b

    produces: ::

        SBBreakpoint: id = 1, file ='main.cpp', line = 66, locations = 1
        SBBreakpoint: id = 2, file ='main.cpp', line = 85, locations = 1

    and, ::

        for wp_loc in target.watchpoint_iter():
            print wp_loc

    produces: ::

        Watchpoint 1: addr = 0x1034ca048 size = 4 state = enabled type = rw
            declare @ '/Volumes/data/lldb/svn/trunk/test/python_api/watchpoint/main.c:12'
            hw_index = 0  hit_count = 2     ignore_count = 0
    """

    

    def __init__(self, rhs: SBTarget = None):
        ...

    @staticmethod
    def GetBroadcasterClassName() -> CString:
        ...

    def IsValid(self) -> bool:
        ...

    @staticmethod
    def EventIsTargetEvent(event: SBEvent) -> bool:
        ...

    @staticmethod
    def GetTargetFromEvent(event: SBEvent) -> SBTarget:
        ...

    @staticmethod
    def GetNumModulesFromEvent(event: SBEvent) -> Int32:
        ...

    @staticmethod
    def GetModuleAtIndexFromEvent(idx: Int32, event: SBEvent) -> SBModule:
        ...

    def GetProcess(self) -> SBProcess:
        ...

    def GetPlatform(self) -> SBPlatform:
        r"""
        GetPlatform(SBTarget self) -> SBPlatform

            Return the platform object associated with the target.

            After return, the platform object should be checked for
            validity.

            @return
                A platform object.
        """
        ...

    def Install(self) -> SBError:
        r"""
        Install(SBTarget self) -> SBError

            Install any binaries that need to be installed.

            This function does nothing when debugging on the host system.
            When connected to remote platforms, the target's main executable
            and any modules that have their install path set will be
            installed on the remote platform. If the main executable doesn't
            have an install location set, it will be installed in the remote
            platform's working directory.

            @return
                An error describing anything that went wrong during
                installation.
        """
        ...

    def LaunchSimple(self, argv: CStringStar, envp: CStringStar, working_directory: CString) -> SBProcess:
        r"""
        LaunchSimple(SBTarget self, char const ** argv, char const ** envp, char const * working_directory) -> SBProcess

            Launch a new process with sensible defaults.

            :param argv: The argument array.
            :param envp: The environment array.
            :param working_directory: The working directory to have the child process run in
            :return: The newly created process.
            :rtype: SBProcess

            A pseudo terminal will be used as stdin/stdout/stderr.
            No launch flags are passed and the target's debuger is used as a listener.

            For example, ::

                process = target.LaunchSimple(['X', 'Y', 'Z'], None, os.getcwd())

            launches a new process by passing 'X', 'Y', 'Z' as the args to the
            executable.
        """
        ...

    def Launch(self, *args) -> SBProcess:
        r"""
        Launch(SBTarget self, SBListener listener, char const ** argv, char const ** envp, char const * stdin_path, char const * stdout_path, char const * stderr_path, char const * working_directory, uint32_t launch_flags, bool stop_at_entry, SBError error) -> SBProcess
        Launch(SBTarget self, SBLaunchInfo launch_info, SBError error) -> SBProcess

            Launch a new process.

            Launch a new process by spawning a new process using the
            target object's executable module's file as the file to launch.
            Arguments are given in argv, and the environment variables
            are in envp. Standard input and output files can be
            optionally re-directed to stdin_path, stdout_path, and
            stderr_path.

            @param[in] listener
                An optional listener that will receive all process events.
                If listener is valid then listener will listen to all
                process events. If not valid, then this target's debugger
                (SBTarget::GetDebugger()) will listen to all process events.

            @param[in] argv
                The argument array.

            @param[in] envp
                The environment array.

            @param[in] launch_flags
                Flags to modify the launch (@see lldb::LaunchFlags)

            @param[in] stdin_path
                The path to use when re-directing the STDIN of the new
                process. If all stdXX_path arguments are NULL, a pseudo
                terminal will be used.

            @param[in] stdout_path
                The path to use when re-directing the STDOUT of the new
                process. If all stdXX_path arguments are NULL, a pseudo
                terminal will be used.

            @param[in] stderr_path
                The path to use when re-directing the STDERR of the new
                process. If all stdXX_path arguments are NULL, a pseudo
                terminal will be used.

            @param[in] working_directory
                The working directory to have the child process run in

            @param[in] launch_flags
                Some launch options specified by logical OR'ing
                lldb::LaunchFlags enumeration values together.

            @param[in] stop_at_entry
                If false do not stop the inferior at the entry point.

            @param[out]
                An error object. Contains the reason if there is some failure.

            @return
                 A process object for the newly created process.

            For example,

                process = target.Launch(self.dbg.GetListener(), None, None,
                                        None, '/tmp/stdout.txt', None,
                                        None, 0, False, error)

            launches a new process by passing nothing for both the args and the envs
            and redirect the standard output of the inferior to the /tmp/stdout.txt
            file. It does not specify a working directory so that the debug server
            will use its idea of what the current working directory is for the
            inferior. Also, we ask the debugger not to stop the inferior at the
            entry point. If no breakpoint is specified for the inferior, it should
            run to completion if no user interaction is required.
        """
        ...

    def LoadCore(self, *args) -> SBProcess:
        r"""
        LoadCore(SBTarget self, char const * core_file) -> SBProcess
        LoadCore(SBTarget self, char const * core_file, SBError error) -> SBProcess

            Load a core file

            @param[in] core_file
                File path of the core dump.

            @param[out] error
                An error explaining what went wrong if the operation fails.
                (Optional)

            @return
                 A process object for the newly created core file.

            For example,

                process = target.LoadCore('./a.out.core')

            loads a new core file and returns the process object.
        """
        ...

    def Attach(self, attach_info: SBAttachInfo, error: SBError) -> SBProcess:
        ...

    def AttachToProcessWithID(self, listener: SBListener, pid: PIDT, error: SBError) -> SBProcess:
        r"""
        AttachToProcessWithID(SBTarget self, SBListener listener, lldb::pid_t pid, SBError error) -> SBProcess

            Attach to process with pid.

            @param[in] listener
                An optional listener that will receive all process events.
                If listener is valid then listener will listen to all
                process events. If not valid, then this target's debugger
                (SBTarget::GetDebugger()) will listen to all process events.

            @param[in] pid
                The process ID to attach to.

            @param[out]
                An error explaining what went wrong if attach fails.

            @return
                 A process object for the attached process.
        """
        ...

    def AttachToProcessWithName(self, listener: SBListener, name: CString, wait_for: bool, error: SBError) -> SBProcess:
        r"""
        AttachToProcessWithName(SBTarget self, SBListener listener, char const * name, bool wait_for, SBError error) -> SBProcess

            Attach to process with name.

            @param[in] listener
                An optional listener that will receive all process events.
                If listener is valid then listener will listen to all
                process events. If not valid, then this target's debugger
                (SBTarget::GetDebugger()) will listen to all process events.

            @param[in] name
                Basename of process to attach to.

            @param[in] wait_for
                If true wait for a new instance of 'name' to be launched.

            @param[out]
                An error explaining what went wrong if attach fails.

            @return
                 A process object for the attached process.
        """
        ...

    def ConnectRemote(self, listener: SBListener, url: CString, plugin_name: CString, error: SBError) -> SBProcess:
        r"""
        ConnectRemote(SBTarget self, SBListener listener, char const * url, char const * plugin_name, SBError error) -> SBProcess

            Connect to a remote debug server with url.

            @param[in] listener
                An optional listener that will receive all process events.
                If listener is valid then listener will listen to all
                process events. If not valid, then this target's debugger
                (SBTarget::GetDebugger()) will listen to all process events.

            @param[in] url
                The url to connect to, e.g., 'connect://localhost:12345'.

            @param[in] plugin_name
                The plugin name to be used; can be NULL.

            @param[out]
                An error explaining what went wrong if the connect fails.

            @return
                 A process object for the connected process.
        """
        ...

    def GetExecutable(self) -> SBFileSpec:
        ...

    def AppendImageSearchPath(self, _from: CString, to: CString, error: SBError) -> None:
        r"""
        AppendImageSearchPath(SBTarget self, char const * _from, char const * to, SBError error)

            Append the path mapping (from -> to) to the target's paths mapping list.
        """
        ...

    def AddModule(self, *args) -> SBModule:
        r"""
        AddModule(SBTarget self, SBModule module) -> bool
        AddModule(SBTarget self, char const * path, char const * triple, char const * uuid) -> SBModule
        AddModule(SBTarget self, char const * path, char const * triple, char const * uuid_cstr, char const * symfile) -> SBModule
        AddModule(SBTarget self, SBModuleSpec module_spec) -> SBModule
        """
        ...

    def GetNumModules(self) -> Int32:
        ...

    def GetModuleAtIndex(self, idx: Int32) -> SBModule:
        ...

    def RemoveModule(self, module: SBModule) -> bool:
        ...

    def GetDebugger(self) -> SBDebugger:
        ...

    def FindModule(self, file_spec: SBFileSpec) -> SBModule:
        ...

    def FindCompileUnits(self, sb_file_spec: "SBFileSpec") -> SBSymbolContextList:
        r"""
        FindCompileUnits(SBTarget self, SBFileSpec sb_file_spec) -> SBSymbolContextList

            Find compile units related to this target and passed source
            file.

            :param sb_file_spec: A :py:class:`lldb::SBFileSpec` object that contains source file
                specification.
            :return: The symbol contexts for all the matches.
            :rtype: SBSymbolContextList
        """
        ...

    def GetByteOrder(self) -> ByteOrder:
        ...

    def GetAddressByteSize(self) -> Int32:
        ...

    def GetTriple(self) -> CString:
        ...

    def GetDataByteSize(self) -> Int32:
        r"""
        GetDataByteSize(SBTarget self) -> uint32_t

            Architecture data byte width accessor

            :return: The size in 8-bit (host) bytes of a minimum addressable unit from the Architecture's data bus.


        """
        ...

    def GetCodeByteSize(self) -> Int32:
        r"""
        GetCodeByteSize(SBTarget self) -> uint32_t

            Architecture code byte width accessor.

            :return: The size in 8-bit (host) bytes of a minimum addressable unit from the Architecture's code bus.


        """
        return ...

    def SetSectionLoadAddress(self, section: SBSection, section_base_addr: AddressT) -> SBError:
        ...

    def ClearSectionLoadAddress(self, section: SBSection) -> SBError:
        ...

    def SetModuleLoadAddress(self, module: SBModule, sections_offset: Int64) -> SBError:
        ...

    def ClearModuleLoadAddress(self, module: SBModule) -> SBError:
        ...

    def FindFunctions(self, *args) -> SBSymbolContextList:
        r"""
        FindFunctions(SBTarget self, char const * name, uint32_t name_type_mask=eFunctionNameTypeAny) -> SBSymbolContextList

            Find functions by name.

            :param name: The name of the function we are looking for.

            :param name_type_mask:
                A logical OR of one or more FunctionNameType enum bits that
                indicate what kind of names should be used when doing the
                lookup. Bits include fully qualified names, base names,
                C++ methods, or ObjC selectors.
                See FunctionNameType for more details.

            :return:
                A lldb::SBSymbolContextList that gets filled in with all of
                the symbol contexts for all the matches.
        """
        ...

    def FindFirstType(self, type: CString) -> SBType:
        ...

    def FindTypes(self, type: CString) -> SBTypeList:
        ...

    def GetBasicType(self, type: BasicType) -> SBType:
        ...

    def GetSourceManager(self) -> SBSourceManager:
       ...

    def FindFirstGlobalVariable(self, name: CString) -> SBValue:
        r"""
        FindFirstGlobalVariable(SBTarget self, char const * name) -> SBValue

            Find the first global (or static) variable by name.

            @param[in] name
                The name of the global or static variable we are looking
                for.

            @return
                An SBValue that gets filled in with the found variable (if any).
        """
        ...

    def FindGlobalVariables(self, *args) -> SBValueList:
        r"""
        FindGlobalVariables(SBTarget self, char const * name, uint32_t max_matches) -> SBValueList
        FindGlobalVariables(SBTarget self, char const * name, uint32_t max_matches, lldb::MatchType matchtype) -> SBValueList

            Find global and static variables by name.

            @param[in] name
                The name of the global or static variable we are looking
                for.

            @param[in] max_matches
                Allow the number of matches to be limited to max_matches.

            @return
                A list of matched variables in an SBValueList.
        """
        ...

    def FindGlobalFunctions(self, name: CString, max_matches: Int32, matchtype: MatchType) -> SBSymbolContextList:
        ...

    def Clear(self) -> None:
        ...

    def ResolveFileAddress(self, file_addr: AddressT) -> SBAddress:
        r"""
        ResolveFileAddress(SBTarget self, lldb::addr_t file_addr) -> SBAddress

            Resolve a current file address into a section offset address.

            @param[in] file_addr

            @return
                An SBAddress which will be valid if...
        """
        ...

    def ResolveLoadAddress(self, vm_addr: AddressT) -> SBAddress:
        ...

    def ResolvePastLoadAddress(self, stop_id: Int32, vm_addr: AddressT) -> SBAddress:
        ...

    def ResolveSymbolContextForAddress(self, addr: SBAddress, resolve_scope: Int32) -> SBSymbolContext:
        ...

    def ReadMemory(self, addr: SBAddress, buf: VoidStar, error: SBError) -> SizeT:
        r"""
        ReadMemory(SBTarget self, SBAddress addr, void * buf, SBError error) -> size_t

            Read target memory. If a target process is running then memory
            is read from here. Otherwise the memory is read from the object
            files. For a target whose bytes are sized as a multiple of host
            bytes, the data read back will preserve the target's byte order.

            @param[in] addr
                A target address to read from.

            @param[out] buf
                The buffer to read memory into.

            @param[in] size
                The maximum number of host bytes to read in the buffer passed
                into this call

            @param[out] error
                Error information is written here if the memory read fails.

            @return
                The amount of data read in host bytes.
        """
        ...

    def BreakpointCreateByLocation(self, *args) -> SBBreakpoint:
        r"""
        BreakpointCreateByLocation(SBTarget self, char const * file, uint32_t line) -> SBBreakpoint
        BreakpointCreateByLocation(SBTarget self, SBFileSpec file_spec, uint32_t line) -> SBBreakpoint
        BreakpointCreateByLocation(SBTarget self, SBFileSpec file_spec, uint32_t line, lldb::addr_t offset) -> SBBreakpoint
        BreakpointCreateByLocation(SBTarget self, SBFileSpec file_spec, uint32_t line, lldb::addr_t offset, SBFileSpecList module_list) -> SBBreakpoint
        BreakpointCreateByLocation(SBTarget self, SBFileSpec file_spec, uint32_t line, uint32_t column, lldb::addr_t offset, SBFileSpecList module_list) -> SBBreakpoint
        BreakpointCreateByLocation(SBTarget self, SBFileSpec file_spec, uint32_t line, uint32_t column, lldb::addr_t offset, SBFileSpecList module_list, bool move_to_nearest_code) -> SBBreakpoint
        """
        ...

    def BreakpointCreateByName(self, *args) -> SBBreakpoint:
        r"""
        BreakpointCreateByName(SBTarget self, char const * symbol_name, char const * module_name=None) -> SBBreakpoint
        BreakpointCreateByName(SBTarget self, char const * symbol_name, uint32_t func_name_type, SBFileSpecList module_list, SBFileSpecList comp_unit_list) -> SBBreakpoint
        BreakpointCreateByName(SBTarget self, char const * symbol_name, uint32_t func_name_type, lldb::LanguageType symbol_language, SBFileSpecList module_list, SBFileSpecList comp_unit_list) -> SBBreakpoint
        """
        ...

    def BreakpointCreateByNames(self, *args) -> SBBreakpoint:
        r"""
        BreakpointCreateByNames(SBTarget self, char const ** symbol_name, uint32_t name_type_mask, SBFileSpecList module_list, SBFileSpecList comp_unit_list) -> SBBreakpoint
        BreakpointCreateByNames(SBTarget self, char const ** symbol_name, uint32_t name_type_mask, lldb::LanguageType symbol_language, SBFileSpecList module_list, SBFileSpecList comp_unit_list) -> SBBreakpoint
        BreakpointCreateByNames(SBTarget self, char const ** symbol_name, uint32_t name_type_mask, lldb::LanguageType symbol_language, lldb::addr_t offset, SBFileSpecList module_list, SBFileSpecList comp_unit_list) -> SBBreakpoint
        """
        ...

    def BreakpointCreateByRegex(self, *args) -> SBBreakpoint:
        r"""
        BreakpointCreateByRegex(SBTarget self, char const * symbol_name_regex, char const * module_name=None) -> SBBreakpoint
        BreakpointCreateByRegex(SBTarget self, char const * symbol_name_regex, lldb::LanguageType symbol_language, SBFileSpecList module_list, SBFileSpecList comp_unit_list) -> SBBreakpoint
        """
        ...

    def BreakpointCreateBySourceRegex(self, *args) -> SBBreakpoint:
        r"""
        BreakpointCreateBySourceRegex(SBTarget self, char const * source_regex, SBFileSpec source_file, char const * module_name=None) -> SBBreakpoint
        BreakpointCreateBySourceRegex(SBTarget self, char const * source_regex, SBFileSpecList module_list, SBFileSpecList file_list) -> SBBreakpoint
        BreakpointCreateBySourceRegex(SBTarget self, char const * source_regex, SBFileSpecList module_list, SBFileSpecList source_file, SBStringList func_names) -> SBBreakpoint
        """
        ...

    def BreakpointCreateForException(self, language: LanguageType, catch_bp: bool, throw_bp: bool) -> SBBreakpoint:
        ...

    def BreakpointCreateByAddress(self, address: AddressT) -> SBBreakpoint:
        ...

    def GetEnvironment(self) -> SBEnvironment:
        ...

    def BreakpointCreateBySBAddress(self, sb_address: SBAddress) -> SBBreakpoint:
        ...

    def BreakpointCreateFromScript(self, class_name: CString, extra_args: SBStructuredData, module_list: SBFileSpecList, file_list: SBFileSpecList, request_hardware: bool=False) -> SBBreakpoint:
        r"""
        BreakpointCreateFromScript(SBTarget self, char const * class_name, SBStructuredData extra_args, SBFileSpecList module_list, SBFileSpecList file_list, bool request_hardware=False) -> SBBreakpoint

            Create a breakpoint using a scripted resolver.

            @param[in] class_name
               This is the name of the class that implements a scripted resolver.
               The class should have the following signature: ::

                   class Resolver:
                       def __init__(self, bkpt, extra_args):
                           # bkpt - the breakpoint for which this is the resolver.  When
                           # the resolver finds an interesting address, call AddLocation
                           # on this breakpoint to add it.
                           #
                           # extra_args - an SBStructuredData that can be used to
                           # parametrize this instance.  Same as the extra_args passed
                           # to BreakpointCreateFromScript.

                       def __get_depth__ (self):
                           # This is optional, but if defined, you should return the
                           # depth at which you want the callback to be called.  The
                           # available options are:
                           #    lldb.eSearchDepthModule
                           #    lldb.eSearchDepthCompUnit
                           # The default if you don't implement this method is
                           # eSearchDepthModule.

                       def __callback__(self, sym_ctx):
                           # sym_ctx - an SBSymbolContext that is the cursor in the
                           # search through the program to resolve breakpoints.
                           # The sym_ctx will be filled out to the depth requested in
                           # __get_depth__.
                           # Look in this sym_ctx for new breakpoint locations,
                           # and if found use bkpt.AddLocation to add them.
                           # Note, you will only get called for modules/compile_units that
                           # pass the SearchFilter provided by the module_list & file_list
                           # passed into BreakpointCreateFromScript.

                       def get_short_help(self):
                           # Optional, but if implemented return a short string that will
                           # be printed at the beginning of the break list output for the
                           # breakpoint.

            @param[in] extra_args
               This is an SBStructuredData object that will get passed to the
               constructor of the class in class_name.  You can use this to
               reuse the same class, parametrizing it with entries from this
               dictionary.

            @param module_list
               If this is non-empty, this will be used as the module filter in the
               SearchFilter created for this breakpoint.

            @param file_list
               If this is non-empty, this will be used as the comp unit filter in the
               SearchFilter created for this breakpoint.

            @return
                An SBBreakpoint that will set locations based on the logic in the
                resolver's search callback.
        """
        ...

    def GetNumBreakpoints(self) -> Int32:
        ...

    def GetBreakpointAtIndex(self, idx: Int32) -> SBBreakpoint:
        ...

    def BreakpointDelete(self, break_id: BreakIdT) -> bool:
        ...

    def FindBreakpointByID(self, break_id: BreakIdT) -> SBBreakpoint:
        ...

    def FindBreakpointsByName(self, name: CString, bkpt_list: SBBreakpointList) -> bool:
        ...

    def DeleteBreakpointName(self, name: CString) -> None:
        ...

    def GetBreakpointNames(self, names: SBStringList) -> None:
        ...

    def EnableAllBreakpoints(self) -> bool:
        ...

    def DisableAllBreakpoints(self) -> bool:
        ...

    def DeleteAllBreakpoints(self) -> bool:
        ...

    def BreakpointsCreateFromFile(self, *args) -> SBError:
        r"""
        BreakpointsCreateFromFile(SBTarget self, SBFileSpec source_file, SBBreakpointList bkpt_list) -> SBError
        BreakpointsCreateFromFile(SBTarget self, SBFileSpec source_file, SBStringList matching_names, SBBreakpointList new_bps) -> SBError

            Read breakpoints from source_file and return the newly created
            breakpoints in bkpt_list.

            @param[in] source_file
               The file from which to read the breakpoints

            @param[in] matching_names
               Only read in breakpoints whose names match one of the names in this
               list.

            @param[out] bkpt_list
               A list of the newly created breakpoints.

            @return
                An SBError detailing any errors in reading in the breakpoints.
        """
        ...

    def BreakpointsWriteToFile(self, *args) -> SBError:
        r"""
        BreakpointsWriteToFile(SBTarget self, SBFileSpec dest_file) -> SBError
        BreakpointsWriteToFile(SBTarget self, SBFileSpec dest_file, SBBreakpointList bkpt_list, bool append=False) -> SBError
        """
        ...

    def GetNumWatchpoints(self) -> Int32:
        ...

    def GetWatchpointAtIndex(self, idx: Int32) -> SBWatchpoint:
        ...

    def DeleteWatchpoint(self, watch_id: WatchIdT) -> bool:
        ...

    def FindWatchpointByID(self, watch_id: WatchIdT) -> SBWatchpoint:
        ...

    def EnableAllWatchpoints(self) -> bool:
        ...

    def DisableAllWatchpoints(self) -> bool:
        ...

    def DeleteAllWatchpoints(self) -> bool:
        ...

    def WatchAddress(self, addr: AddressT, size: SizeT, read: bool, write: bool, error: SBError) -> SBWatchpoint:
        ...

    def GetBroadcaster(self) -> SBBroadcaster:
        ...

    def CreateValueFromAddress(self, name: CString, addr: SBAddress, type: SBType) -> SBValue:
        r"""
        CreateValueFromAddress(SBTarget self, char const * name, SBAddress addr, SBType type) -> SBValue

            Create an SBValue with the given name by treating the memory starting at addr as an entity of type.

            @param[in] name
                The name of the resultant SBValue

            @param[in] addr
                The address of the start of the memory region to be used.

            @param[in] type
                The type to use to interpret the memory starting at addr.

            @return
                An SBValue of the given type, may be invalid if there was an error reading
                the underlying memory.
        """
        ...

    def CreateValueFromData(self, name: CString, data: SBData, type: SBType) -> SBValue:
        ...

    def CreateValueFromExpression(self, name: CString, expr: CString) -> SBValue:
        ...

    def ReadInstructions(self, *args) -> SBInstructionList:
        r"""
        ReadInstructions(SBTarget self, SBAddress base_addr, uint32_t count) -> SBInstructionList
        ReadInstructions(SBTarget self, SBAddress base_addr, uint32_t count, char const * flavor_string) -> SBInstructionList

            Disassemble a specified number of instructions starting at an address.

            :param base_addr: the address to start disassembly from.
            :param count: the number of instructions to disassemble.
            :param flavor_string: may be 'intel' or 'att' on x86 targets to specify that style of disassembly.
            :rtype: SBInstructionList

        """
        ...

    def GetInstructions(self, base_addr: SBAddress, buf: VoidStar) -> SBInstructionList:
        ...

    def GetInstructionsWithFlavor(self, base_addr: SBAddress, flavor_string: CString, buf: VoidStar) -> SBInstructionList:
        r"""
        GetInstructionsWithFlavor(SBTarget self, SBAddress base_addr, char const * flavor_string, void const * buf) -> SBInstructionList

            Disassemble the bytes in a buffer and return them in an SBInstructionList, with a supplied flavor.

            :param base_addr: used for symbolicating the offsets in the byte stream when disassembling.
            :param flavor:  may be 'intel' or 'att' on x86 targets to specify that style of disassembly.
            :param buf: bytes to be disassembled.
            :param size: (C++) size of the buffer.
            :rtype: SBInstructionList

        """
        ...

    def FindSymbols(self, *args) -> SBSymbolContextList:
        ...

    def GetDescription(self, description: SBStream, description_level: DescriptionLevel) -> bool:
        ...

    def GetStackRedZoneSize(self) -> AddressT:
        ...

    def IsLoaded(self, module: SBModule) -> bool:
        r"""
        IsLoaded(SBTarget self, SBModule module) -> bool

            Returns true if the module has been loaded in this `SBTarget`.
            A module can be loaded either by the dynamic loader or by being manually
            added to the target (see `SBTarget.AddModule` and the `target module add` command).

            :rtype: bool

        """
        ...

    def GetLaunchInfo(self) -> SBLaunchInfo:
        ...

    def SetLaunchInfo(self, launch_info: SBLaunchInfo) -> None:
        ...

    def SetCollectingStats(self, v: bool) -> None:
        ...

    def GetCollectingStats(self) -> bool:
        ...

    def GetStatistics(self) -> SBStructuredData:
        ...

    def __eq__(self, rhs: SBTarget) -> bool:
        ...

    def __ne__(self, rhs: SBTarget) -> bool:
        ...

    def EvaluateExpression(self, *args) -> SBValue:
        r"""
        EvaluateExpression(SBTarget self, char const * expr) -> SBValue
        EvaluateExpression(SBTarget self, char const * expr, SBExpressionOptions options) -> SBValue
        """
        ...

    def __str__(self) -> str:
        ...

    def GetTrace(self) -> SBTrace:
        ...

    def CreateTrace(self, error: SBError) -> SBTrace:
        ...

    class modules_access(object):
        '''A helper object that will lazily hand out lldb.SBModule objects for a target when supplied an index, or by full or partial path.'''
        def __init__(self, sbtarget):
            """self.sbtarget = sbtarget"""
            ...

        def __len__(self):
            """if self.sbtarget:
                return int(self.sbtarget.GetNumModules())
            return 0
            """
            ...

        def __getitem__(self, key):
            """num_modules = self.sbtarget.GetNumModules()
            if type(key) is int:
                if key < num_modules:
                    return self.sbtarget.GetModuleAtIndex(key)
            elif type(key) is str:
                if key.find('/') == -1:
                    for idx in range(num_modules):
                        module = self.sbtarget.GetModuleAtIndex(idx)
                        if module.file.basename == key:
                            return module
                else:
                    for idx in range(num_modules):
                        module = self.sbtarget.GetModuleAtIndex(idx)
                        if module.file.fullpath == key:
                            return module
    # See if the string is a UUID
                try:
                    the_uuid = uuid.UUID(key)
                    if the_uuid:
                        for idx in range(num_modules):
                            module = self.sbtarget.GetModuleAtIndex(idx)
                            if module.uuid == the_uuid:
                                return module
                except:
                    return None
            elif type(key) is uuid.UUID:
                for idx in range(num_modules):
                    module = self.sbtarget.GetModuleAtIndex(idx)
                    if module.uuid == key:
                        return module
            elif type(key) is re.SRE_Pattern:
                matching_modules = []
                for idx in range(num_modules):
                    module = self.sbtarget.GetModuleAtIndex(idx)
                    re_match = key.search(module.path.fullpath)
                    if re_match:
                        matching_modules.append(module)
                return matching_modules
            else:
                print("error: unsupported item type: %s" % type(key))
            return None"""
            ...


    def get_modules_access_object(self ) -> modules_access:
        '''An accessor function that returns a modules_access() object which allows lazy module access from a lldb.SBTarget object.'''
        ...

    def get_modules_array(self) -> List[SBModule]:
        '''An accessor function that returns a list() that contains all modules in a lldb.SBTarget object.'''
        """modules = []
        for idx in range(self.GetNumModules()):
            modules.append(self.GetModuleAtIndex(idx))
        return modules"""

    def module_iter(self) -> Iterable[SBModule]:
        '''Returns an iterator over all modules in a lldb.SBTarget
        object.'''
        ...

    def breakpoint_iter(self) -> Iterable[SBBreakpoint]:
        '''Returns an iterator over all breakpoints in a lldb.SBTarget
        object.'''
        ...

    def watchpoint_iter(self) -> Iterable[SBWatchpoint]:
        '''Returns an iterator over all watchpoints in a lldb.SBTarget
        object.'''
        ...

    modules = property(get_modules_array, None, doc='''A read only property that returns a list() of lldb.SBModule objects contained in this target. This list is a list all modules that the target currently is tracking (the main executable and all dependent shared libraries).''')
    module = property(get_modules_access_object, None, doc=r'''A read only property that returns an object that implements python operator overloading with the square brackets().\n    target.module[<int>] allows array access to any modules.\n    target.module[<str>] allows access to modules by basename, full path, or uuid string value.\n    target.module[uuid.UUID()] allows module access by UUID.\n    target.module[re] allows module access using a regular expression that matches the module full path.''')
    process = property(GetProcess, None, doc='''A read only property that returns an lldb object that represents the process (lldb.SBProcess) that this target owns.''')
    executable = property(GetExecutable, None, doc='''A read only property that returns an lldb object that represents the main executable module (lldb.SBModule) for this target.''')
    debugger = property(GetDebugger, None, doc='''A read only property that returns an lldb object that represents the debugger (lldb.SBDebugger) that owns this target.''')
    num_breakpoints = property(GetNumBreakpoints, None, doc='''A read only property that returns the number of breakpoints that this target has as an integer.''')
    num_watchpoints = property(GetNumWatchpoints, None, doc='''A read only property that returns the number of watchpoints that this target has as an integer.''')
    broadcaster = property(GetBroadcaster, None, doc='''A read only property that an lldb object that represents the broadcaster (lldb.SBBroadcaster) for this target.''')
    byte_order = property(GetByteOrder, None, doc='''A read only property that returns an lldb enumeration value (lldb.eByteOrderLittle, lldb.eByteOrderBig, lldb.eByteOrderInvalid) that represents the byte order for this target.''')
    addr_size = property(GetAddressByteSize, None, doc='''A read only property that returns the size in bytes of an address for this target.''')
    triple = property(GetTriple, None, doc='''A read only property that returns the target triple (arch-vendor-os) for this target as a string.''')
    data_byte_size = property(GetDataByteSize, None, doc='''A read only property that returns the size in host bytes of a byte in the data address space for this target.''')
    code_byte_size = property(GetCodeByteSize, None, doc='''A read only property that returns the size in host bytes of a byte in the code address space for this target.''')
    platform = property(GetPlatform, None, doc='''A read only property that returns the platform associated with with this target.''')




class SBSymbol(object):
    r"""
    Represents the symbol possibly associated with a stack frame.
    :py:class:`SBModule` contains SBSymbol(s). SBSymbol can also be retrieved from :py:class:`SBFrame` .
    """

    def __init__(self, *args):
        r"""
        __init__(SBSymbol self) -> SBSymbol
        __init__(SBSymbol self, SBSymbol rhs) -> SBSymbol
        """
        ...

    def IsValid(self) -> bool:
        r"""IsValid(SBSymbol self) -> bool"""
        ...

    



    def GetName(self) -> CString:
        ...

    def GetDisplayName(self) -> CString:
        ...

    def GetMangledName(self) -> CString:
        ...

    def GetInstructions(self, *args) -> SBInstructionList:
        r"""
        GetInstructions(SBSymbol self, SBTarget target) -> SBInstructionList
        GetInstructions(SBSymbol self, SBTarget target, char const * flavor_string) -> SBInstructionList
        """
        ...

    def GetStartAddress(self) -> SBAddress:
        ...

    def GetEndAddress(self) -> SBAddress:
        ...

    def GetPrologueByteSize(self) -> Int32:
        ...

    def GetType(self) -> SymbolType:
        ...

    def GetDescription(self, description: SBStream) -> bool:
        ...

    def IsExternal(self) -> bool:
        ...

    def IsSynthetic(self) -> bool:
        ...

    def __eq__(self, rhs: SBSymbol) -> bool:
        ...

    def __ne__(self, rhs: SBSymbol) -> bool:
        ...

    def __str__(self) -> str:
        ...

    def get_instructions_from_current_target (self):
        """return self.GetInstructions (target)"""
        ...

    name = property(GetName, None, doc='''A read only property that returns the name for this symbol as a string.''')
    mangled = property(GetMangledName, None, doc='''A read only property that returns the mangled (linkage) name for this symbol as a string.''')
    type = property(GetType, None, doc='''A read only property that returns an lldb enumeration value (see enumerations that start with "lldb.eSymbolType") that represents the type of this symbol.''')
    addr = property(GetStartAddress, None, doc='''A read only property that returns an lldb object that represents the start address (lldb.SBAddress) for this symbol.''')
    end_addr = property(GetEndAddress, None, doc='''A read only property that returns an lldb object that represents the end address (lldb.SBAddress) for this symbol.''')
    prologue_size = property(GetPrologueByteSize, None, doc='''A read only property that returns the size in bytes of the prologue instructions as an unsigned integer.''')
    instructions = property(get_instructions_from_current_target, None, doc='''A read only property that returns an lldb object that represents the instructions (lldb.SBInstructionList) for this symbol.''')
    external = property(IsExternal, None, doc='''A read only property that returns a boolean value that indicates if this symbol is externally visiable (exported) from the module that contains it.''')
    synthetic = property(IsSynthetic, None, doc='''A read only property that returns a boolean value that indicates if this symbol was synthetically created from information in module that contains it.''')

class SBSymbolContext(object):
    r"""
    A context object that provides access to core debugger entities.

    Many debugger functions require a context when doing lookups. This class
    provides a common structure that can be used as the result of a query that
    can contain a single result.

    For example, ::

            exe = os.path.join(os.getcwd(), 'a.out')

            # Create a target for the debugger.
            target = self.dbg.CreateTarget(exe)

            # Now create a breakpoint on main.c by name 'c'.
            breakpoint = target.BreakpointCreateByName('c', 'a.out')

            # Now launch the process, and do not stop at entry point.
            process = target.LaunchSimple(None, None, os.getcwd())

            # The inferior should stop on 'c'.
            from lldbutil import get_stopped_thread
            thread = get_stopped_thread(process, lldb.eStopReasonBreakpoint)
            frame0 = thread.GetFrameAtIndex(0)

            # Now get the SBSymbolContext from this frame.  We want everything. :-)
            context = frame0.GetSymbolContext(lldb.eSymbolContextEverything)

            # Get the module.
            module = context.GetModule()
            ...

            # And the compile unit associated with the frame.
            compileUnit = context.GetCompileUnit()
            ...

    """


    def __init__(self, *args):
        r"""
        __init__(SBSymbolContext self) -> SBSymbolContext
        __init__(SBSymbolContext self, SBSymbolContext rhs) -> SBSymbolContext
        """
        ...

    def IsValid(self) -> bool:
        ...


    def GetModule(self) -> SBModule:
        ...

    def GetCompileUnit(self) -> SBCompileUnit:
        ...

    def GetFunction(self) -> SBFunction:
        ...

    def GetBlock(self) -> SBBlock:
        ...

    def GetLineEntry(self) -> SBLineEntry:
        ...

    def GetSymbol(self) -> SBSymbol:
        ...

    def SetModule(self, module: "SBModule") -> None:
        ...

    def SetCompileUnit(self, compile_unit: SBCompileUnit) -> None:
        ...

    def SetFunction(self, function: SBFunction) -> None:
        ...

    def SetBlock(self, block: SBBlock) -> None:
        ...

    def SetLineEntry(self, line_entry: SBLineEntry) -> None:
        ...

    def SetSymbol(self, symbol: SBSymbol) -> None:
        ...

    def GetParentOfInlinedScope(self, curr_frame_pc: SBAddress, parent_frame_addr: SBAddress) -> SBSymbolContext:
        ...

    def GetDescription(self, description: SBStream) -> bool:
        ...

    def __str__(self) -> str:
        ...

    module = property(GetModule, SetModule, doc='''A read/write property that allows the getting/setting of the module (lldb.SBModule) in this symbol context.''')
    compile_unit = property(GetCompileUnit, SetCompileUnit, doc='''A read/write property that allows the getting/setting of the compile unit (lldb.SBCompileUnit) in this symbol context.''')
    function = property(GetFunction, SetFunction, doc='''A read/write property that allows the getting/setting of the function (lldb.SBFunction) in this symbol context.''')
    block = property(GetBlock, SetBlock, doc='''A read/write property that allows the getting/setting of the block (lldb.SBBlock) in this symbol context.''')
    symbol = property(GetSymbol, SetSymbol, doc='''A read/write property that allows the getting/setting of the symbol (lldb.SBSymbol) in this symbol context.''')
    line_entry = property(GetLineEntry, SetLineEntry, doc='''A read/write property that allows the getting/setting of the line entry (lldb.SBLineEntry) in this symbol context.''')

class ByteOrder:
    ...
class SBTypeSummary:
    ...

class UserIdT:
    ...
class AddressT:
    ...
class Int32:
    ...
class Int64:
    ...
class Int8:
    
    ...
class Int16:
    ...
class SizeT:
    ...
class Format:
    ...
class ValueType:
    ...

class SBType:
    ...

class SBStream:
    r"""
    Represents a destination for streaming data output to. By default, a string
    stream is created.

    For example (from test/source-manager/TestSourceManager.py), ::

            # Create the filespec for 'main.c'.
            filespec = lldb.SBFileSpec('main.c', False)
            source_mgr = self.dbg.GetSourceManager()
            # Use a string stream as the destination.
            stream = lldb.SBStream()
            source_mgr.DisplaySourceLinesWithLineNumbers(filespec,
                                                         self.line,
                                                         2, # context before
                                                         2, # context after
                                                         '=>', # prefix for current line
                                                         stream)

            #    2
            #    3    int main(int argc, char const *argv[]) {
            # => 4        printf('Hello world.\n'); // Set break point at this line.
            #    5        return 0;
            #    6    }
            self.expect(stream.GetData(), 'Source code displayed correctly',
                        exe=False,
                patterns = ['=> %d.*Hello world' % self.line])
    """


    def __init__(self):
        ...

    def IsValid(self) -> bool:
        ...


    def GetData(self) -> CString:
        r"""
        GetData(SBStream self) -> char const *

            If this stream is not redirected to a file, it will maintain a local
            cache for the stream data which can be accessed using this accessor.
        """
        ...

    def GetSize(self) -> SizeT:
        r"""
        GetSize(SBStream self) -> size_t

            If this stream is not redirected to a file, it will maintain a local
            cache for the stream output whose length can be accessed using this
            accessor.
        """
        ...

    def Print(self, str: str) -> None:
        ...

    def RedirectToFile(self, *args) -> None:
        r"""
        RedirectToFile(SBStream self, char const * path, bool append)
        RedirectToFile(SBStream self, SBFile file)
        RedirectToFile(SBStream self, lldb::FileSP file)
        """
        ...


    
    def Clear(self) -> None:
        r"""
        DEPRECATED, use RedirectToFile

            If the stream is redirected to a file, forget about the file and if
            ownership of the file was transferred to this object, close the file.
            If the stream is backed by a local cache, clear this cache.
        """
        ...

    def write(self, str: str) -> None:
        ...

    def flush(self) -> None:
        ...

class SBTypeSummaryOptions:
    ...

class DynamicValueType:
    ...

class SBTypeFilter:
    ...

class VoidStar:
    ...

class SBTypeSynthetic:
    ...

class SBExpressionOptions:
    ...

class SBDeclaration:
    ...
class SBProcess:
    ...

class OffsetT:
    ...
class LongDouble:
    ...
class SBThread:
    ...

class SBFrame:
    ...

class SBWatchpoint:
    ...

class SBAddress:
    ...

class CString:
    ...

class SBValue(object):
    r"""
    Represents the value of a variable, a register, or an expression.

    SBValue supports iteration through its child, which in turn is represented
    as an SBValue.  For example, we can get the general purpose registers of a
    frame as an SBValue, and iterate through all the registers,::

        registerSet = frame.registers # Returns an SBValueList.
        for regs in registerSet:
            if 'general purpose registers' in regs.name.lower():
                GPRs = regs
                break

        print('%s (number of children = %d):' % (GPRs.name, GPRs.num_children))
        for reg in GPRs:
            print('Name: ', reg.name, ' Value: ', reg.value)

    produces the output: ::

        General Purpose Registers (number of children = 21):
        Name:  rax  Value:  0x0000000100000c5c
        Name:  rbx  Value:  0x0000000000000000
        Name:  rcx  Value:  0x00007fff5fbffec0
        Name:  rdx  Value:  0x00007fff5fbffeb8
        Name:  rdi  Value:  0x0000000000000001
        Name:  rsi  Value:  0x00007fff5fbffea8
        Name:  rbp  Value:  0x00007fff5fbffe80
        Name:  rsp  Value:  0x00007fff5fbffe60
        Name:  r8  Value:  0x0000000008668682
        Name:  r9  Value:  0x0000000000000000
        Name:  r10  Value:  0x0000000000001200
        Name:  r11  Value:  0x0000000000000206
        Name:  r12  Value:  0x0000000000000000
        Name:  r13  Value:  0x0000000000000000
        Name:  r14  Value:  0x0000000000000000
        Name:  r15  Value:  0x0000000000000000
        Name:  rip  Value:  0x0000000100000dae
        Name:  rflags  Value:  0x0000000000000206
        Name:  cs  Value:  0x0000000000000027
        Name:  fs  Value:  0x0000000000000010
        Name:  gs  Value:  0x0000000000000048

    See also linked_list_iter() for another perspective on how to iterate through an
    SBValue instance which interprets the value object as representing the head of a
    linked list.
    """

    def __init__(self, rhs : SBValue = None):
        ...

    def IsValid(self) -> bool:
        ...

    def __nonzero__(self):
        ...
    

    def Clear(self) -> None:
        ...

    def GetError(self) -> SBError:
        ...

    def GetID(self) -> UserIdT:
        ...
        

    def GetName(self) -> CString:
        ...


    def GetTypeName(self) -> CString:
        ...
        

    def GetDisplayTypeName(self) -> CString:
        ...

    def GetByteSize(self) -> SizeT:
        ...
        

    def IsInScope(self) -> bool:
        ...


    def GetFormat(self) -> Format:
        ...

    def SetFormat(self, format: Format) -> None:
        ...

    def GetValue(self) -> CString:
        ...

    def GetValueAsSigned(self, error: SBError , fail_value : int = 0) -> int:
        ...

    def GetValueAsUnsigned(self, error: SBError , fail_value : int = 0) -> int:
        ...

    def GetValueType(self) -> ValueType:
        ...

    def GetValueDidChange(self) -> bool:
        ...

    def GetSummary(self, stream : SBStream = None , options: SBTypeSummaryOptions = None) -> CString:
        ...

    def GetObjectDescription(self) -> CString:
        ...
        

    def GetDynamicValue(self, use_dynamic: DynamicValueType) -> SBValue:
        ...

    def GetStaticValue(self) -> SBValue:
        ...

    def GetNonSyntheticValue(self) -> SBValue:
        ...

    def GetPreferDynamicValue(self) -> DynamicValueType:
        ...

    def SetPreferDynamicValue(self, use_dynamic: DynamicValueType) -> None:
        ...

    def GetPreferSyntheticValue(self) -> bool:
        ...

    def SetPreferSyntheticValue(self, use_synthetic: bool) -> None:
        ...

    def IsDynamic(self) -> bool:
        ...

    def IsSynthetic(self) -> bool:
        ...

    def IsSyntheticChildrenGenerated(self) -> bool:
        ...

    def SetSyntheticChildrenGenerated(self, arg2: bool) -> None:
        ...

    def GetLocation(self) -> CString:
        ...

    def SetValueFromCString(self, value : CString  , error: SBError) -> bool:
        ...

    def GetTypeFormat(self) -> SbTypeFormat:
        ...

    def GetTypeSummary(self) -> SBTypeSummary:
        ...

    def GetTypeFilter(self) -> SBTypeFilter:
        ...

    def GetTypeSynthetic(self) -> SBTypeSynthetic:
        ...

    def GetChildAtIndex(self, idx: int , use_dynamic: DynamicValueType ,  can_create_synthetic: bool) -> SBValue:
        r"""
        GetChildAtIndex(SBValue self, uint32_t idx) -> SBValue
        GetChildAtIndex(SBValue self, uint32_t idx, lldb::DynamicValueType use_dynamic, bool can_create_synthetic) -> SBValue

            Get a child value by index from a value.

            Structs, unions, classes, arrays and pointers have child
            values that can be access by index.

            Structs and unions access child members using a zero based index
            for each child member. For

            Classes reserve the first indexes for base classes that have
            members (empty base classes are omitted), and all members of the
            current class will then follow the base classes.

            Pointers differ depending on what they point to. If the pointer
            points to a simple type, the child at index zero
            is the only child value available, unless synthetic_allowed
            is true, in which case the pointer will be used as an array
            and can create 'synthetic' child values using positive or
            negative indexes. If the pointer points to an aggregate type
            (an array, class, union, struct), then the pointee is
            transparently skipped and any children are going to be the indexes
            of the child values within the aggregate type. For example if
            we have a 'Point' type and we have a SBValue that contains a
            pointer to a 'Point' type, then the child at index zero will be
            the 'x' member, and the child at index 1 will be the 'y' member
            (the child at index zero won't be a 'Point' instance).

            If you actually need an SBValue that represents the type pointed
            to by a SBValue for which GetType().IsPointeeType() returns true,
            regardless of the pointee type, you can do that with the SBValue.Dereference
            method (or the equivalent deref property).

            Arrays have a preset number of children that can be accessed by
            index and will returns invalid child values for indexes that are
            out of bounds unless the synthetic_allowed is true. In this
            case the array can create 'synthetic' child values for indexes
            that aren't in the array bounds using positive or negative
            indexes.

            @param[in] idx
                The index of the child value to get

            @param[in] use_dynamic
                An enumeration that specifies whether to get dynamic values,
                and also if the target can be run to figure out the dynamic
                type of the child value.

            @param[in] synthetic_allowed
                If true, then allow child values to be created by index
                for pointers and arrays for indexes that normally wouldn't
                be allowed.

            @return
                A new SBValue object that represents the child member value.
        """
        ...

    def CreateChildAtOffset(self, name: CString, offset: int, type: SBType) -> SBValue:
        ...

    def Cast(self, type: SBType) -> SBValue:
        ...

    def CreateValueFromExpression(self, name : CString , expression : CString,  options : SBExpressionOptions) -> SBValue:
        ...

    def CreateValueFromAddress(self, name: CString, address: AddressT, type: SBType) -> SBValue:
        ...

    def CreateValueFromData(self, name: CString, data: SBData, type: SBType) -> SBValue:
        ...

    def GetType(self) -> SBType:
        ...

    def GetIndexOfChildWithName(self, name: CString) -> Int32:
        r"""
        GetIndexOfChildWithName(SBValue self, char const * name) -> uint32_t

            Returns the child member index.

            Matches children of this object only and will match base classes and
            member names if this is a clang typed object.

            @param[in] name
                The name of the child value to get

            @return
                An index to the child member value.
        """
        ...

    def GetChildMemberWithName(self, name : CString , use_dynamic : DynamicValueType = None) -> SBValue:
        r"""
        GetChildMemberWithName(SBValue self, char const * name) -> SBValue
        GetChildMemberWithName(SBValue self, char const * name, lldb::DynamicValueType use_dynamic) -> SBValue

            Returns the child member value.

            Matches child members of this object and child members of any base
            classes.

            @param[in] name
                The name of the child value to get

            @param[in] use_dynamic
                An enumeration that specifies whether to get dynamic values,
                and also if the target can be run to figure out the dynamic
                type of the child value.

            @return
                A new SBValue object that represents the child member value.
        """
        ...

    def GetValueForExpressionPath(self, expr_path: CString) -> SBValue:
        r"""
        GetValueForExpressionPath(SBValue self, char const * expr_path) -> SBValue
        Expands nested expressions like .a->b[0].c[1]->d.
        """
        ...

    def GetDeclaration(self) -> SBDeclaration:
        ...

    def MightHaveChildren(self) -> bool:
        ...

    def IsRuntimeSupportValue(self) -> bool:
        ...

    def GetNumChildren(self, max: Int32 = None) -> Int32:
        ...

    def GetOpaqueType(self) -> VoidStar:
        ...

    def Dereference(self) -> SBValue:
        ...

    def AddressOf(self) -> SBValue:
        ...

    def TypeIsPointerType(self) -> bool:
        ...

    def GetTarget(self) -> SBTarget:
        ...

    def GetProcess(self) -> SBProcess:
        ...

    def GetThread(self) -> SBThread:
        ...

    def GetFrame(self) -> SBFrame:
        ...

    def Watch(self, resolve_location: bool, read: bool, write: bool, error: SBError) -> SBWatchpoint:
        r"""
        Watch(SBValue self, bool resolve_location, bool read, bool write, SBError error) -> SBWatchpoint

            Find and watch a variable.
            It returns an SBWatchpoint, which may be invalid.
        """
        ...

    def WatchPointee(self, resolve_location: bool, read: bool, write: bool, error: SBError) -> SBWatchpoint:
        r"""
        WatchPointee(SBValue self, bool resolve_location, bool read, bool write, SBError error) -> SBWatchpoint

            Find and watch the location pointed to by a variable.
            It returns an SBWatchpoint, which may be invalid.
        """
        ...

    def GetDescription(self, description: SBStream) -> bool:
        ...

    def GetPointeeData(self, item_idx: Int32=0, item_count: Int32=1) -> SBData:
        r"""
        GetPointeeData(SBValue self, uint32_t item_idx=0, uint32_t item_count=1) -> SBData

            Get an SBData wrapping what this SBValue points to.

            This method will dereference the current SBValue, if its
            data type is a ``T\*`` or ``T[]``, and extract ``item_count`` elements
            of type ``T`` from it, copying their contents in an :py:class:`SBData`.

            :param item_idx: The index of the first item to retrieve. For an array
                this is equivalent to array[item_idx], for a pointer
                to ``\*(pointer + item_idx)``. In either case, the measurement
                unit for item_idx is the ``sizeof(T)`` rather than the byte
            :param item_count: How many items should be copied into the output. By default
                only one item is copied, but more can be asked for.
            :return: The contents of the copied items on success. An empty :py:class:`SBData` otherwise.
            :rtype: SBData

        """
        ...

    def GetData(self) -> SBData:
        r"""
        GetData(SBValue self) -> SBData

            Get an SBData wrapping the contents of this SBValue.

            This method will read the contents of this object in memory
            and copy them into an SBData for future use.

            @return
                An SBData with the contents of this SBValue, on success.
                An empty SBData otherwise.
        """
        ...

    def SetData(self, data: SBData, error: SBError) -> bool:
        ...

    def GetLoadAddress(self) -> AddressT:
        ...

    def GetAddress(self) -> SBAddress:
        ...

    def Persist(self) -> SBValue:
        ...

    def GetExpressionPath(self, description: SBStream , qualify_cxx_base_classes: bool = None) -> bool:
        ...

    def EvaluateExpression(self, expression: CString , options : SBExpressionOptions , name : str) -> SBValue:
        r"""
        EvaluateExpression(SBValue self, char const * expr) -> SBValue
        EvaluateExpression(SBValue self, char const * expr, SBExpressionOptions options) -> SBValue
        EvaluateExpression(SBValue self, char const * expr, SBExpressionOptions options, char const * name) -> SBValue
        """
        ...

    def __str__(self) -> str:
        ...

    def __get_dynamic__ (self):
        '''Helper function for the "SBValue.dynamic" property.'''
        ...

    class children_access(object):
        '''A helper object that will lazily hand out thread for a process when supplied an index.'''

        def __init__(self, sbvalue):
            self.sbvalue = sbvalue

        def __len__(self):
            if self.sbvalue:
                return int(self.sbvalue.GetNumChildren())
            return 0

        def __getitem__(self, key) -> SBValue:
            if type(key) is int and key < len(self):
                return self.sbvalue.GetChildAtIndex(key)
            return None

    def get_child_access_object(self) -> children_access:
        '''An accessor function that returns a children_access() object which allows lazy member variable access from a lldb.SBValue object.'''
        return self.children_access (self)

    def get_value_child_list(self) -> list[SBValue]:
        '''An accessor function that returns a list() that contains all children in a lldb.SBValue object.'''
        children = []
        accessor = self.get_child_access_object()
        for idx in range(len(accessor)):
            children.append(accessor[idx])
        return children

    def __iter__(self) -> list[SBValue]:
        ...

    def __len__(self) -> int:
        '''Return the number of child values of a lldb.SBValue object.'''
        ...

    children = property(get_value_child_list, None, doc='''A read only property that returns a list() of lldb.SBValue objects for the children of the value.''')
    child = property(get_child_access_object, None, doc='''A read only property that returns an object that can access children of a variable by index (child_value = value.children[12]).''')
    name = property(GetName, None, doc='''A read only property that returns the name of this value as a string.''')
    type = property(GetType, None, doc='''A read only property that returns a lldb.SBType object that represents the type for this value.''')
    size = property(GetByteSize, None, doc='''A read only property that returns the size in bytes of this value.''')
    is_in_scope = property(IsInScope, None, doc='''A read only property that returns a boolean value that indicates whether this value is currently lexically in scope.''')
    format = property(GetName, SetFormat, doc='''A read/write property that gets/sets the format used for lldb.SBValue().GetValue() for this value. See enumerations that start with "lldb.eFormat".''')
    value = property(GetValue, SetValueFromCString, doc='''A read/write property that gets/sets value from a string.''')
    value_type = property(GetValueType, None, doc='''A read only property that returns an lldb enumeration value (see enumerations that start with "lldb.eValueType") that represents the type of this value (local, argument, global, register, etc.).''')
    changed = property(GetValueDidChange, None, doc='''A read only property that returns a boolean value that indicates if this value has changed since it was last updated.''')
    data = property(GetData, None, doc='''A read only property that returns an lldb object (lldb.SBData) that represents the bytes that make up the value for this object.''')
    load_addr = property(GetLoadAddress, None, doc='''A read only property that returns the load address of this value as an integer.''')
    addr = property(GetAddress, None, doc='''A read only property that returns an lldb.SBAddress that represents the address of this value if it is in memory.''')
    deref = property(Dereference, None, doc='''A read only property that returns an lldb.SBValue that is created by dereferencing this value.''')
    address_of = property(AddressOf, None, doc='''A read only property that returns an lldb.SBValue that represents the address-of this value.''')
    error = property(GetError, None, doc='''A read only property that returns the lldb.SBError that represents the error from the last time the variable value was calculated.''')
    summary = property(GetSummary, None, doc='''A read only property that returns the summary for this value as a string''')
    description = property(GetObjectDescription, None, doc='''A read only property that returns the language-specific description of this value as a string''')
    dynamic = property(__get_dynamic__, None, doc='''A read only property that returns an lldb.SBValue that is created by finding the dynamic type of this value.''')
    location = property(GetLocation, None, doc='''A read only property that returns the location of this value as a string.''')
    target = property(GetTarget, None, doc='''A read only property that returns the lldb.SBTarget that this value is associated with.''')
    process = property(GetProcess, None, doc='''A read only property that returns the lldb.SBProcess that this value is associated with, the returned value might be invalid and should be tested.''')
    thread = property(GetThread, None, doc='''A read only property that returns the lldb.SBThread that this value is associated with, the returned value might be invalid and should be tested.''')
    frame = property(GetFrame, None, doc='''A read only property that returns the lldb.SBFrame that this value is associated with, the returned value might be invalid and should be tested.''')
    num_children = property(GetNumChildren, None, doc='''A read only property that returns the number of child lldb.SBValues that this value has.''')
    unsigned = property(GetValueAsUnsigned, None, doc='''A read only property that returns the value of this SBValue as an usigned integer.''')
    signed = property(GetValueAsSigned, None, doc='''A read only property that returns the value of this SBValue as a signed integer.''')

    def get_expr_path(self) -> SBData:
        s = SBStream()
        self.GetExpressionPath (s)
        return s.GetData()

    path = property(get_expr_path, None, doc='''A read only property that returns the expression path that one can use to reach this value in an expression.''')

    def synthetic_child_from_expression(self, name, expr, options=None) -> SBValue:

        """
        if options is None: options = lldb.SBExpressionOptions()
        child = self.CreateValueFromExpression(name, expr, options)
        child.SetSyntheticChildrenGenerated(True)
        return child
        """
        ...

    def synthetic_child_from_data(self, name, data, type) -> SBValue:
        """
        child = self.CreateValueFromData(name, data, type)
        child.SetSyntheticChildrenGenerated(True)
        return child
        """
        ...

        

    def synthetic_child_from_address(self, name, addr, type) -> SBValue:
        """
        child = self.CreateValueFromAddress(name, addr, type)
        child.SetSyntheticChildrenGenerated(True)
        return child
        """
        ...

    def __eol_test(val):
        """Default function for end of list test takes an SBValue object.

        Return True if val is invalid or it corresponds to a null pointer.
        Otherwise, return False.
        """
        """
        if not val or val.GetValueAsUnsigned() == 0:
            return True
        else:
            return False
            """
        ...
        

    # ==================================================
    # Iterator for lldb.SBValue treated as a linked list
    # ==================================================
    def linked_list_iter(self, next_item_name, end_of_list_test=__eol_test):
        """Generator adaptor to support iteration for SBValue as a linked list.

        linked_list_iter() is a special purpose iterator to treat the SBValue as
        the head of a list data structure, where you specify the child member
        name which points to the next item on the list and you specify the
        end-of-list test function which takes an SBValue for an item and returns
        True if EOL is reached and False if not.

        linked_list_iter() also detects infinite loop and bails out early.

        The end_of_list_test arg, if omitted, defaults to the __eol_test
        function above.

        For example,

    # Get Frame #0.
        ...

    # Get variable 'task_head'.
        task_head = frame0.FindVariable('task_head')
        ...

        for t in task_head.linked_list_iter('next'):
            print t
        """
        """
        if end_of_list_test(self):
            return
        item = self
        visited = set()
        try:
            while not end_of_list_test(item) and not item.GetValueAsUnsigned() in visited:
                visited.add(item.GetValueAsUnsigned())
                yield item
    # Prepare for the next iteration.
                item = item.GetChildMemberWithName(next_item_name)
        except:
    # Exception occurred.  Stop the generator.
            pass

        return
        """
        ...

class SBValueList(object):
    r"""
    Represents a collection of SBValues.  Both :py:class:`SBFrame.GetVariables()` and
    :py:class:`SBFrame.GetRegisters()` return a SBValueList.

    SBValueList supports :py:class:`SBValue` iteration. For example (from test/lldbutil.py),::

        def get_registers(frame, kind):
            '''Returns the registers given the frame and the kind of registers desired.

            Returns None if there's no such kind.
            '''
            registerSet = frame.GetRegisters() # Return type of SBValueList.
            for value in registerSet:
                if kind.lower() in value.GetName().lower():
                    return value

            return None

        def get_GPRs(frame):
            '''Returns the general purpose registers of the frame as an SBValue.

            The returned SBValue object is iterable.  An example:
                ...
                from lldbutil import get_GPRs
                regs = get_GPRs(frame)
                for reg in regs:
                    print('%s => %s' % (reg.GetName(), reg.GetValue()))
                ...
            '''
            return get_registers(frame, 'general purpose')

        def get_FPRs(frame):
            '''Returns the floating point registers of the frame as an SBValue.

            The returned SBValue object is iterable.  An example:
                ...
                from lldbutil import get_FPRs
                regs = get_FPRs(frame)
                for reg in regs:
                    print('%s => %s' % (reg.GetName(), reg.GetValue()))
                ...
            '''
            return get_registers(frame, 'floating point')

        def get_ESRs(frame):
            '''Returns the exception state registers of the frame as an SBValue.

            The returned SBValue object is iterable.  An example:
                ...
                from lldbutil import get_ESRs
                regs = get_ESRs(frame)
                for reg in regs:
                    print('%s => %s' % (reg.GetName(), reg.GetValue()))
                ...
            '''
            return get_registers(frame, 'exception state')

    """

    ...

class SBData(object):
    r"""Represents a data buffer."""


    def __init__(self, rhs: SBData):
        ...

    def GetAddressByteSize(self) -> Int8:
        ...

    def SetAddressByteSize(self, addr_byte_size: Int8) -> None:
        ...

    def Clear(self) -> None:
        ...

    def IsValid(self) -> bool:
        ...

    def GetByteSize(self) -> SizeT:
        ...

    def GetByteOrder(self) -> ByteOrder:
        ...

    def SetByteOrder(self, endian: ByteOrder) -> None:
        ...

    def GetFloat(self, error: SBError, offset: OffsetT) -> float:
        ...


    def GetDouble(self, error: SBError, offset: OffsetT) -> double:
        ...

    def GetLongDouble(self, error: SBError, offset: OffsetT) -> LongDouble:
        ...

    def GetAddress(self, error: SBError, offset: OffsetT) -> AddressT:
        ...

    def GetUnsignedInt8(self, error: SBError, offset: OffsetT) -> Int8:
        ...

    def GetUnsignedInt16(self, error: SBError, offset: OffsetT) -> Int16:
        ...

    def GetUnsignedInt32(self, error: SBError, offset: OffsetT) -> Int32:
        ...

    def GetUnsignedInt64(self, error: SBError, offset: OffsetT) -> Int64:
        ...

    def GetSignedInt8(self, error: SBError, offset: OffsetT) -> Int8:
        ...

    def GetSignedInt16(self, error: SBError, offset: OffsetT) -> Int16:
        ...

    def GetSignedInt32(self, error: SBError, offset: OffsetT) -> Int32:
        ...

    def GetSignedInt64(self, error: SBError, offset: OffsetT) -> Int64:
        ...

    def GetString(self, error: SBError, offset: OffsetT) -> CString:
        ...

    def GetDescription(self, description: SBStream, base_addr: AddressT) -> bool:
        ...

    def ReadRawData(self, error: SBError, offset: OffsetT, buf: VoidStar) -> SizeT:
        ...

    def SetData(self, error: SBError, buf: VoidStar, endian: ByteOrder, addr_size: Int8) -> None:
        ...

    def Append(self, rhs: "SBData") -> bool:
        ...

    @staticmethod
    def CreateDataFromCString(endian: ByteOrder, addr_byte_size: Int32, data: CString) -> SBData:
        ...

    @staticmethod
    def CreateDataFromUInt64Array(endian: ByteOrder, addr_byte_size: Int32, array: List[Int64]) -> SBData:
        ...

    @staticmethod
    def CreateDataFromUInt32Array(endian: ByteOrder, addr_byte_size: Int32, array: List[Int32]) -> SBData:
        ...

    @staticmethod
    def CreateDataFromSInt64Array(endian: ByteOrder, addr_byte_size: Int32, array: List[Int64]) -> SBData:
        ...

    @staticmethod
    def CreateDataFromSInt32Array(endian: ByteOrder, addr_byte_size: Int32, array: List[Int32]) -> SBData:
        ...

    @staticmethod
    def CreateDataFromDoubleArray(endian: ByteOrder, addr_byte_size: Int32, array: List[float]) -> SBData:
        ...

    def SetDataFromCString(self, data: CString) -> bool:
        ...

    def SetDataFromUInt64Array(self, array: List[Int64]) -> bool:
        ...

    def SetDataFromUInt32Array(self, array: List[Int32]) -> bool:
        ...

    def SetDataFromSInt64Array(self, array: List[Int64]) -> bool:
        ...

    def SetDataFromSInt32Array(self, array: List[Int32]) -> bool:
        ...

    def SetDataFromDoubleArray(self, array: List[float]) -> bool:
        ...


    class read_data_helper:
        def __init__(self, sbdata, readerfunc, item_size):
            """self.sbdata = sbdata
            self.readerfunc = readerfunc
            self.item_size = item_size"""
            ...
        def __getitem__(self,key):
            """if isinstance(key,slice):
                list = []
                for x in range(*key.indices(self.__len__())):
                    list.append(self.__getitem__(x))
                return list
            if not (isinstance(key,six.integer_types)):
                raise TypeError('must be int')
            key = key * self.item_size # SBData uses byte-based indexes, but we want to use itemsize-based indexes here
            error = SBError()
            my_data = self.readerfunc(self.sbdata,error,key)
            if error.Fail():
                raise IndexError(error.GetCString())
            else:
                return my_data"""
            ...
        def __len__(self):
            """return int(self.sbdata.GetByteSize()/self.item_size)"""
            ...
            
        def all(self):
            """return self[0:len(self)]"""
            ...

    @classmethod
    def CreateDataFromInt (cls, value, size = None, target = None, ptr_size = None, endian = None):
        """import sys
        lldbmodule = sys.modules[cls.__module__]
        lldbdict = lldbmodule.__dict__
        if 'target' in lldbdict:
            lldbtarget = lldbdict['target']
        else:
            lldbtarget = None
        if target == None and lldbtarget != None and lldbtarget.IsValid():
            target = lldbtarget
        if ptr_size == None:
            if target and target.IsValid():
                ptr_size = target.addr_size
            else:
                ptr_size = 8
        if endian == None:
            if target and target.IsValid():
                endian = target.byte_order
            else:
                endian = lldbdict['eByteOrderLittle']
        if size == None:
            if value > 2147483647:
                size = 8
            elif value < -2147483648:
                size = 8
            elif value > 4294967295:
                size = 8
            else:
                size = 4
        if size == 4:
            if value < 0:
                return SBData().CreateDataFromSInt32Array(endian, ptr_size, [value])
            return SBData().CreateDataFromUInt32Array(endian, ptr_size, [value])
        if size == 8:
            if value < 0:
                return SBData().CreateDataFromSInt64Array(endian, ptr_size, [value])
            return SBData().CreateDataFromUInt64Array(endian, ptr_size, [value])
        return None
        """
        ...

    def _make_helper(self, sbdata, getfunc, itemsize):
        """
        return self.read_data_helper(sbdata, getfunc, itemsize)
        """
        ...

    def _make_helper_uint8(self):
        """
        return self._make_helper(self, SBData.GetUnsignedInt8, 1)
        """
        ...

    def _make_helper_uint16(self):
        """
        return self._make_helper(self, SBData.GetUnsignedInt16, 2)
        """
        ...

    def _make_helper_uint32(self):
        """
        return self._make_helper(self, SBData.GetUnsignedInt32, 4)
        """
        ...

    def _make_helper_uint64(self):
        """return self._make_helper(self, SBData.GetUnsignedInt64, 8)"""
        ...

    def _make_helper_sint8(self):
        """return self._make_helper(self, SBData.GetSignedInt8, 1)"""
        ...

    def _make_helper_sint16(self):
        """return self._make_helper(self, SBData.GetSignedInt16, 2)"""
        ...

    def _make_helper_sint32(self):
        """return self._make_helper(self, SBData.GetSignedInt32, 4)"""
        ...

    def _make_helper_sint64(self):
        """return self._make_helper(self, SBData.GetSignedInt64, 8)"""
        ...

    def _make_helper_float(self):
        """return self._make_helper(self, SBData.GetFloat, 4)"""
        ...

    def _make_helper_double(self):
        """return self._make_helper(self, SBData.GetDouble, 8)"""
        ...

    def _read_all_uint8(self):
        """return self._make_helper_uint8().all()"""
        ...

    def _read_all_uint16(self):
        """return self._make_helper_uint16().all()"""
        ...

    def _read_all_uint32(self):
        """return self._make_helper_uint32().all()"""
        ...

    def _read_all_uint64(self):
        """return self._make_helper_uint64().all()"""
        ...

    def _read_all_sint8(self):
        """return self._make_helper_sint8().all()"""
        ...

    def _read_all_sint16(self):
        """return self._make_helper_sint16().all()"""
        ...

    def _read_all_sint32(self):
        """return self._make_helper_sint32().all()"""
        ...

    def _read_all_sint64(self):
        """return self._make_helper_sint64().all()"""
        ...

    def _read_all_float(self):
        """return self._make_helper_float().all()"""
        ...

    def _read_all_double(self):
        """return self._make_helper_double().all()"""
        ...

    uint8 = property(_make_helper_uint8, None, doc='''A read only property that returns an array-like object out of which you can read uint8 values.''')
    uint16 = property(_make_helper_uint16, None, doc='''A read only property that returns an array-like object out of which you can read uint16 values.''')
    uint32 = property(_make_helper_uint32, None, doc='''A read only property that returns an array-like object out of which you can read uint32 values.''')
    uint64 = property(_make_helper_uint64, None, doc='''A read only property that returns an array-like object out of which you can read uint64 values.''')
    sint8 = property(_make_helper_sint8, None, doc='''A read only property that returns an array-like object out of which you can read sint8 values.''')
    sint16 = property(_make_helper_sint16, None, doc='''A read only property that returns an array-like object out of which you can read sint16 values.''')
    sint32 = property(_make_helper_sint32, None, doc='''A read only property that returns an array-like object out of which you can read sint32 values.''')
    sint64 = property(_make_helper_sint64, None, doc='''A read only property that returns an array-like object out of which you can read sint64 values.''')
    float = property(_make_helper_float, None, doc='''A read only property that returns an array-like object out of which you can read float values.''')
    double = property(_make_helper_double, None, doc='''A read only property that returns an array-like object out of which you can read double values.''')
    uint8s = property(_read_all_uint8, None, doc='''A read only property that returns an array with all the contents of this SBData represented as uint8 values.''')
    uint16s = property(_read_all_uint16, None, doc='''A read only property that returns an array with all the contents of this SBData represented as uint16 values.''')
    uint32s = property(_read_all_uint32, None, doc='''A read only property that returns an array with all the contents of this SBData represented as uint32 values.''')
    uint64s = property(_read_all_uint64, None, doc='''A read only property that returns an array with all the contents of this SBData represented as uint64 values.''')
    sint8s = property(_read_all_sint8, None, doc='''A read only property that returns an array with all the contents of this SBData represented as sint8 values.''')
    sint16s = property(_read_all_sint16, None, doc='''A read only property that returns an array with all the contents of this SBData represented as sint16 values.''')
    sint32s = property(_read_all_sint32, None, doc='''A read only property that returns an array with all the contents of this SBData represented as sint32 values.''')
    sint64s = property(_read_all_sint64, None, doc='''A read only property that returns an array with all the contents of this SBData represented as sint64 values.''')
    floats = property(_read_all_float, None, doc='''A read only property that returns an array with all the contents of this SBData represented as float values.''')
    doubles = property(_read_all_double, None, doc='''A read only property that returns an array with all the contents of this SBData represented as double values.''')
    byte_order = property(GetByteOrder, SetByteOrder, doc='''A read/write property getting and setting the endianness of this SBData (data.byte_order = lldb.eByteOrderLittle).''')
    size = property(GetByteSize, None, doc='''A read only property that returns the size the same result as GetByteSize().''')
