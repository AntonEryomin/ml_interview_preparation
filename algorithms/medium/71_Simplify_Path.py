class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []
        crnt_folder = []

        for smb in path:
            if smb == "/":
                if len(crnt_folder) > 0:
                    word = "".join(crnt_folder)
                    if word == ".":
                        pass
                    else:
                        folders.append(word)
                crnt_folder = []
            else:
                crnt_folder.append(smb)

        if len(crnt_folder) > 0:
            word = "".join(crnt_folder)
            if word != ".":
                folders.append(word)

        final_folders = []
        for word in folders:
            if word != '..':
                final_folders.append(word)
            else:
                if len(final_folders) > 0:
                    final_folders.pop()

        if len(final_folders) == 0:
            return "/"
        else:
            return "/" + "/".join(final_folders)
