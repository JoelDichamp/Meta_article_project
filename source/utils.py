import pathlib 

EXT_NOTES = ".docx"
EXT_PDF = ".pdf"
EXT_TAGS = ".json"
FILE_TAGS = "tags" + EXT_TAGS
FCT_CREATE = "create"
FCT_UPDATE = "update"

D_PATH_ARTICLE = "pathArticle"
D_TAGS = "tags"
D_PATH_TAGS = "pathTags"
D_PDF = "pdf"
D_PATH_PDF = "pathPdf"
D_NOTES = "notes"
D_PATH_NOTES = "pathNotes"

COL_ARTICLE = 0
COL_TAGS = 1
COL_PDF = 2
COL_NOTES = 3

WORD_BOUNDARY = r'\b'

currentDir = pathlib.Path(__file__).resolve().parent
dataFolder = currentDir.parent / "data"
# print(current_dir, data_folder)