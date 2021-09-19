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

if currentDir.stem == "source":
  dataFolder = currentDir.parent / "data"
else:
  # si on fait un exe, il n'y a pas le dir source
  dataFolder = currentDir / "data"

dataFolder.mkdir(exist_ok=True)