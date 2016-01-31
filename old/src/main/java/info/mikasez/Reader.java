package info.mikasez;

import info.mikasez.processors.FileProcessor;
import info.mikasez.processors.exception.ProcessException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.logging.Logger;

/**
 * A file reader which call an action for each line in a file
 */
@Service
public class Reader {
    public static final Logger log = Logger.getLogger(Reader.class.getName());
    private String content;
    @Autowired
    private FileProcessor processor;

    public Reader(FileProcessor fp) {
        this.processor = fp;
    }


    public void readFile(String path) {
        try {
            BufferedReader reader = Files.newBufferedReader(Paths.get(path), Charset.forName("utf-8"));
            reader.lines().forEach(l -> {
                try {
                    processor.process(l);
                } catch (ProcessException e) {
                    log.severe(e.getMessage());
                }
            });
        } catch (IOException e) {
            log.severe("couldn't read specified source file : " + path);
        }
    }
}
