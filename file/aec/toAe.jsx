var sc_file = new File($.fileName)
var sc_path = sc_file.path
var aec_path = sc_path+"/snailBox_temp.aec"
var aec_file = new File(aec_path)
var importOptions = new ImportOptions(aec_file);
importOptions.fileType = "aec";
app.project.importFile(importOptions);