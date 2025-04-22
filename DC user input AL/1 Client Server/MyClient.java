import java.io.*;
import java.net.*;
import java.util.Scanner;

public class MyClient {
public static void main(String[] args) {
try{	
Socket s=new Socket("localhost",6666);
	
DataOutputStream dout=new DataOutputStream(s.getOutputStream());
Scanner sc = new Scanner(System.in);
String inp = sc.next();
dout.writeUTF(inp);
dout.flush();
sc.close();
dout.close();
s.close();

}catch(Exception e){System.out.println(e);}
}
}