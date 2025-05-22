import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ClienteJava {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 12345);
            System.out.println("🟢 Conectado al servidor");

            // Hilo para recibir mensajes
            new Thread(() -> {
                try {
                    BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    String mensaje;
                    while ((mensaje = entrada.readLine()) != null) {
                        System.out.println("\n📩 " + mensaje);
                    }
                } catch (IOException e) {
                    System.out.println("❌ Error al recibir mensaje.");
                }
            }).start();

            // Enviar mensajes
            PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.print("> ");
                String msg = scanner.nextLine();
                salida.println(msg);
            }

        } catch (IOException e) {
            System.out.println("❌ Error de conexión: " + e.getMessage());
        }
    }
}
