package info.mikasez.processors.properties;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by MikaSez on 15/10/2015.
 */
public class MDPreprocessor {

    private Queue<Line> lines = new LinkedList<>();


    public void process(FileInputStream stream) {
        assert (stream != null) : "un contenu de fichier valide doit être passé à cette methode";
        BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
        reader.lines().forEach(r ->
                        lines.add(new Line(MdProcessor.isMultiline(r), r))
        );

    }

    public Queue<Line> getProcessed() {
        return lines;
    }
}
