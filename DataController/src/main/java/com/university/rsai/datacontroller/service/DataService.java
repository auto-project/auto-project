package com.university.rsai.datacontroller.service;

import net.schmizz.sshj.SSHClient;
import net.schmizz.sshj.sftp.RemoteResourceInfo;
import net.schmizz.sshj.sftp.SFTPClient;
import net.schmizz.sshj.transport.verification.PromiscuousVerifier;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class DataService {
    private final String resourceFile = "/tmp/diag_storage.txt";
    private final String separator = "/n";
    private String line = "";

    public List<String> readSensorInformation() {
        return readRemoteFileInformation();
    }
    private List<String> readRemoteFileInformation(){
        List<String> sensorInfo = new ArrayList<>();
        File fp = new File(resourceFile);
        if(!fp.exists()){
            return sensorInfo;
        }
        try(BufferedReader br = new BufferedReader(new FileReader(resourceFile))){
            while((line=br.readLine())!=null){
                String[] fileInfo = line.split(separator);
                sensorInfo.add(fileInfo[0]);
            }
        }catch(IOException e){
            System.out.println(e);
        }
        return  sensorInfo;
    }

}
