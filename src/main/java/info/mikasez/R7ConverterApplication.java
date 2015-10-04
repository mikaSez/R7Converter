package info.mikasez;

import info.mikasez.interpreters.CommandLineInterpreter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.util.Map;

@SpringBootApplication
public class R7ConverterApplication {


    @Autowired
    CommandLineInterpreter interpreter;

    public static void main(String[] args) {
        SpringApplication.run(R7ConverterApplication.class, args);
    }

    @Bean
    CommandLineRunner lookup() {
        return arg -> {

            for (String s : arg) {
                interpreter.add(s);
            }
            Map.Entry entry = interpreter.process();
        };
    }
}
