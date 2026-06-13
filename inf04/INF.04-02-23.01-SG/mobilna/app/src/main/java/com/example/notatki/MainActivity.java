package com.example.notatki;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    ArrayAdapter<String> notesAdapter;
    ArrayList<String> notes = new ArrayList<>();

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

        TextView input = findViewById(R.id.input);
        ListView list = findViewById(R.id.notes_list);

        notes.add("Zakupy: chleb, masło, ser");
        notes.add("Do zrobienia: obiad, umyć podłogi");
        notes.add("weekend: kino, spacer z psem");

        notesAdapter = new ArrayAdapter<>(this, R.layout.item, R.id.list_item, notes);
        list.setAdapter(notesAdapter);

        findViewById(R.id.btn_add).setOnClickListener(l -> {
            String text = input.getText().toString();

            if(text.isEmpty()) {
                return;
            }

            notes.add(text);
            notesAdapter.notifyDataSetChanged();
        });
    }
}