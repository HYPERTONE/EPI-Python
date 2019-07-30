
# A file or directory can be specified via a string called the pathname. This string may specify an absolute path, starting from the root
# e.g., /usr/bin/gcc, or a path relative to the current working directory, e.g., scripts/awkscripts

# The same directory may be specified by multiple directory paths. For example, /usr/lib/../bin/gcc and
# scripts//./../scripts/awkscripts/././ specify equivalent absolute and relative pathnames. 

# Write a program which takes a pathname, and returns the shortest equivalent pathname. Assume individual directories and files 
# have names that use only alphanumeric characters. Subdirectory names may be combined using forward slashes (/), the current
# directory (.), and parent directory (..).

def shortest_equivalent_path(path):
    if not path:
        raise ValueError('Empty string is not a valid path.')
    
    path_names = []
    # Special case: / is an absolute path so we can't go up from it
    if path[0] == '/':
        path_names.append('/')
    
    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        else:
            path_names.append(token)
    
    result = '/'.join(path_names)
    return result[result.startswith('//'):] # True = 1 and False = 0 
                                            # so the first two // are ignored

myDir = "sc//./../tc/awk/././"
# from a starting folder, we go into sc. // doesn't do anything, it is just
# historical compatibility. One dot is current folder. Two dots goes up a directory.
# so we went into sc and came back out, then we went into tc/awk. 

print(shortest_equivalent_path(myDir)) # -> tc/awk


