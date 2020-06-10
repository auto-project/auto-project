package com.university.rsai.datacontroller.controller;

import com.university.rsai.datacontroller.service.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.ws.rs.Produces;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@RestController
public class Controller {
    private final DataService dataService;


    @Autowired
    public Controller(DataService dataService) {
        this.dataService = dataService;
    }

    @GetMapping(value="/sensor/information")
    @Produces("application/json")
    public List<String> whenDownloadFileUsingSshj_thenSuccess(){
         return dataService.readSensorInformation();
    }

    @GetMapping(value="/health", produces = "application/json")
    public String viewHealth(){
        return "OK";
    }

}
