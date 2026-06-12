package com.example.myapplication;

import android.os.Bundle;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    static String[] QUOTES = {
            "Dzień dobry",
            "Good morgning",
            "Buenos dias"
    };

    int quotePos = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);

        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        TextView lblSize = findViewById(R.id.lbl_size);
        SeekBar slider = findViewById(R.id.slider);
        TextView lblQuote = findViewById(R.id.lbl_quote);
        Button button = findViewById(R.id.btn);

        slider.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                lblSize.setText("Rozmiar: " + i);
                lblQuote.setTextSize(i);
                button.setTextSize(i);
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {}
            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {}
        });

        button.setOnClickListener(l -> {
            quotePos = (quotePos + 1) % QUOTES.length;
            lblQuote.setText(QUOTES[quotePos]);
        });
    }
}