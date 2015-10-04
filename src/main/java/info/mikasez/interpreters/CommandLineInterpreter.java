package info.mikasez.interpreters;

import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.AbstractMap;
import java.util.Map;
import java.util.Queue;
import java.util.concurrent.ArrayBlockingQueue;

/**
 * Created by MikaSez on 04/10/2015.
 * Simple command line iterpreter <br>
 * It focuses itself on finding from and target filepaths.<br>
 * Standart input is : -f //<fileName//> -t //<fileName//>
 */

//TODO Add argument for conversion result  - > MD / EAST / RJS
@Service
public class CommandLineInterpreter {
    Queue<String> commands = new ArrayBlockingQueue<>(4);
    String source;
    String target;

    /**
     * Adds commandline parameters to the queue.
     * It will ignore all
     */
    public void add(String s) {
        if (s.contains("--spring")) return;
        try {
            commands.add(s);
        } catch (IllegalStateException e) {
            throw new IllegalArgumentException(e);
        }
    }


    /**
     * This methods should be called after {@link #add} <br>
     * It will return a couple of values representing from and target file <br>
     * If arguments count is 3 it will search for both commands -t and -f <br>
     * If arguments count is 2 it will process as there is no commands and from-file comes first <br>
     * If <strong>from file doesn't exist</strong> it will throw a {@link IllegalArgumentException} <br>
     * If <strong>argument number isn't 3 or 2</strong> it will throw an {@link IllegalArgumentException} <br>
     * if <strong>target file already exists </strong>  it will throw an {@link IllegalArgumentException} <br>
     *
     * @return Entry\\\<FromFile, TargetFile\\>
     * @throws IllegalArgumentException
     */
    public Map.Entry process() {
        if (commands.size() != 3 && commands.size() != 2) {
            throw new IllegalArgumentException("Invalid argument count :" + commands.size());
        }
        if (commands.size() == 3) {
            process4();
        } else {
            process2();
        }
        assert (source != null && target != null) : "source and target files should both exist";
        return new AbstractMap.SimpleEntry(source, target);
    }


    /**
     * Processor for 2 arguments calls
     */
    private void process2() {
        assert (commands.size() == 2) : "argument size should be 2";
        processSourceFile(commands.poll());
        processTargetFile(commands.poll());
    }

    /**
     * Processor for 3 arguments calls
     */
    private void process4() {
        assert (commands.size() == 3) : "argument size should be 3";
        String s = commands.poll();
        if (s.equals("-t")) {
            processTargetFile(commands.poll());
            processSourceFile(commands.poll());

        } else if (s.equals("-f")) {
            processSourceFile(commands.poll());
            processTargetFile(commands.poll());
        }
    }

    /**
     * should be a path <br>
     * should exist <br>
     * should be a file <br>
     * should be readable
     *
     * @throws IllegalArgumentException
     */
    private void processSourceFile(String source) {
        Path path = Paths.get(source);
        if (path.toFile().isFile() && path.toFile().canRead()) {
            this.source = path.toString();
        } else {
            throw new IllegalArgumentException("Source file should exist and be readable : " + path);
        }

    }

    /**
     * should be a path <br>
     * should be writable <br>
     * should not exist
     *
     * @throws IllegalArgumentException
     */
    private void processTargetFile(String target) {
        Path path = Paths.get(target);
        if (path.toFile().exists()) {
            throw new IllegalArgumentException("A file or a directory with this name already exists: " + path);
        }
        try {
            if (!path.toFile().createNewFile()) {
                throw new IllegalArgumentException("Couldn't create target file : " + path);
            }
            this.target = path.toString();

        } catch (IOException e) {
            throw new IllegalArgumentException("Target path should be writable :" + path);
        }
    }
}
