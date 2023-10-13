import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Timer;
import java.util.TimerTask;

public class SensorService extends Service implements SensorEventListener {
    // ...

    private Timer fileWriteTimer;
    private BufferedWriter fileWriter;

    @Override
    public void onCreate() {
        super.onCreate();
        // ...

        // Start the timer to write to file every second
        fileWriteTimer = new Timer();
        fileWriteTimer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                writeFilteredZValuesToFile();
            }
        }, 1000, 1000);
    }

    private void writeFilteredZValuesToFile() {
        // Get the filtered "z" values
        float[] filteredValues = kFilter.getFilteredValues();

        // Create a file to write the values
        File file = new File(getFilesDir(), "filtered_z_values.txt");

        try {
            // Create a FileWriter and BufferedWriter to write to the file
            fileWriter = new BufferedWriter(new FileWriter(file, true));

            // Write the filtered "z" values to the file
            for (float value : filteredValues) {
                fileWriter.write(String.valueOf(value));
                fileWriter.newLine();
            }

            // Flush and close the writer
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // ...
}
