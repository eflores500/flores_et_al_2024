// User dialogue to select main directory
mainDir = getDirectory("Choose a Directory");

// Get list of all items (files/folders) in the main directory
items = getFileList(mainDir);

run("Set Measurements...", "area mean standard redirect=None decimal=3");

for (j = 0; j < items.length; j++) {
    // Construct the path for the item
    itemPath = mainDir + items[j];

    // Check if the item is a directory (subfolder)
    if (File.isDirectory(itemPath)) {
        dir = itemPath + "/";
        list = getFileList(dir);

        for (i = 0; i < list.length; i++) {
            filename = list[i];
            open(dir + filename);
            run("StackReg", "transformation=[Rigid Body]");
            run("Duplicate...", "duplicate channels=1");
            rename("mask");
            setThreshold(850, 65535);
            setOption("BlackBackground", false);
            run("Convert to Mask");
            run("Watershed");
            run("Analyze Particles...", "size=200-50000 circularity=0-.718 exclude add");
            selectWindow("mask");
            close();
            selectWindow(filename);
            roiManager("Select All");
            roiManager("Multi Measure");
            saveAs("Results", dir + filename + ".csv");
            roiManager("Delete");
            selectWindow(filename);
            close();
        }
    }
}
