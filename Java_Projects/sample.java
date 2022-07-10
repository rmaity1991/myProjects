import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'decryptMessage' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING encryptedMessage as parameter.
     */

    public static String decryptMessage(String encryptedMessage) {

        String mystring = encryptedMessage;
        String result = "";
        String finalresult = "";

        char temp = '\0';
        char temp1 = '\0';
        int j;

        for (int i = 0; i < mystring.length(); i++) {

            temp = mystring.charAt(i);

            switch (temp) {

                case '0':
                    break;

                case '1':
                    break;

                case '2':

                    j = 1;

                    while (j < 2) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                case '3':

                    j = 1;

                    while (j < 3) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                case '4':
                    j = 1;

                    while (j < 4) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                case '5':
                    j = 1;

                    while (j < 5) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                case '6':
                    j = 1;

                    while (j < 6) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                case '7':

                    j = 1;

                    while (j < 7) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                case '8':
                    j = 1;

                    while (j < 8) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                case '9':

                    j = 1;

                    while (j < 9) {
                        temp1 = mystring.charAt(i - 1);
                        result.concat(Character.toString(temp1));
                        j++;
                    }
                    break;

                default:
                    result.concat(Character.toString(temp1));
                    break;

            }

        }

        for (j = mystring.length(); j > -1; j--) {

            temp = result.charAt(j);
            finalresult.concat(Character.toString(temp));

        }

        return finalresult;

    }

}

public class sample {
    public static void main(String[] args) {

        String result = Result.decryptMessage("world hel20");

        System.out.println(result);
    }
}