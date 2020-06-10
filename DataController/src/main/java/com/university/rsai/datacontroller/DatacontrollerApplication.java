package com.university.rsai.datacontroller;

import net.schmizz.sshj.SSHClient;
import net.schmizz.sshj.transport.verification.PromiscuousVerifier;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.IOException;

@SpringBootApplication
public class DatacontrollerApplication {

    public static void main(String[] args) {
        SpringApplication.run(DatacontrollerApplication.class, args);
    }

}