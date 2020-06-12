# Communication between DTC Forwarding and HMI

## Description and functionality
The functionality of DataController is to read from /tmp/diag_storage.txt file information that come from DTC team and to bring it to HMI team.
In DataController there is functionality, which read the information saved in the file and it exposes endpoint, which HMI team cah access on port 8080.
The functionality which this application provides, is executed on raspberry.
Technologies that are used for writing the app are: Spring and Java.

### Setup communnication
1. Download jdk8 and Extract the jdk-8u241-linux-x64.tar.gz file in that directory using this command:  
```sudo tar -xvzf ~/Downloads/jdk-8u241-linux-x64.tar.gz```
2. Configure java path. Add the following environment variables at the end of the file.
```JAVA_HOME="/usr/lib/jvm/jdk1.8.0_241"```
```Path="/usr/lib/jvm/jdk1.8.0_241/jre/bin"```
3. Download Maven and Extract the apache-maven archive into the opt directory.
```cd /opt ```
```udo tar -xvzf ~/Downloads/apache-maven-3.6.3-bin.tar.gz```
4. dit the /etc/environment file and add the following environment variable:
```M2_HOME="/opt/apache-maven-3.6.3"```
```Path=/opt/apache-maven-3.6.3/bin```
5. Now you should execute jar file in raspberry. Execute following commands:
```cd /home/pi/```
```java -jar datacontroller-0.0.1.SNAPSHOT.jar```

### Information for clients
This command will execute application and it will enable you to read information from /tmp/diag_storage.txt file, when you browse this http link:
http://localhost:8080/sensor/information.
The endpoint of a Data Controller returns JSON format:
`[U0001,U0002]`

One important thing to note is that the DTCs are in the following format: 
**One leading capital letter followed by 4 digits**. For a full specification you'd 
have to contact the DTC team.
