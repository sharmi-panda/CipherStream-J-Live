import java.io.*;
import java.util.Random;

/**
 * FileCipher: A Byte-Level Cryptographic Engine
 * This class handles raw byte transformation, allowing for the 
 * encryption of any data type, including Emojis and Symbols.
 */
public class FileCipher {
    public static void main(String[] args) {
    String mode = (args.length > 0) ? args[0] : "encrypt";
    
    try {
        if (mode.equals("generate-key")) {
            generateKeyFile("vault.key");
        } else {
            // Check if key exists before reading
            File keyFile = new File("vault.key");
            if (!keyFile.exists()) {
                System.err.println("Error: vault.key not found in " + keyFile.getAbsolutePath());
                System.exit(1); // Tells Python "I failed"
            }

            int key = readKeyFromFile("vault.key");
            int shift = mode.equals("encrypt") ? key : -key;
            
            String input = mode.equals("encrypt") ? "plain.txt" : "encrypted.txt";
            String output = mode.equals("encrypt") ? "encrypted.txt" : "decrypted_result.txt";
            
            processBytes(input, output, shift);
        }
    } catch (Exception e) {
        System.err.println("Java Runtime Error: " + e.getMessage());
        System.exit(1); 
    }
}

    /**
     * Generates a random integer key and saves it to a file.
     * This acts as the "Physical Key" for the vault.
     */
    public static void generateKeyFile(String fileName) throws IOException {
        Random random = new Random();
        // Generate a non-zero shift between 1 and 255
        int randomShift = random.nextInt(254) + 1; 
        try (FileWriter writer = new FileWriter(fileName)) {
            writer.write(String.valueOf(randomShift));
        }
    }

    /**
     * Reads the integer shift value from the generated key file.
     */
    public static int readKeyFromFile(String fileName) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String keyStr = reader.readLine();
            if (keyStr == null) throw new IOException("Key file is empty.");
            return Integer.parseInt(keyStr.trim());
        }
    }

    /**
     * The Core Engine: Processes data at the byte level.
     * This ensures compatibility with all UTF-8 characters.
     */
    public static void processBytes(String src, String dest, int shift) throws IOException {
        File inputFile = new File(src);
        if (!inputFile.exists()) {
            throw new FileNotFoundException("Source file not found: " + src);
        }

        try (FileInputStream fis = new FileInputStream(src);
             FileOutputStream fos = new FileOutputStream(dest)) {
            
            int byteData;
            while ((byteData = fis.read()) != -1) {
                // Apply the shift and wrap within the 0-255 byte range
                int transformed = (byteData + shift) % 256;
                
                // Handle negative results for decryption wrap-around
                if (transformed < 0) {
                    transformed += 256;
                }
                
                fos.write(transformed);
            }
        }
    }
}