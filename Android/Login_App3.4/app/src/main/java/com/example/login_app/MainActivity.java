package com.example.login_app;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    //학번 받아오는 뷰
    private TextView tv_id;

    //출석부, 탈퇴버튼
    private Button btn_Attend;
    private Button btn_Out;
    private Button btn_upload1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tv_id = findViewById(R.id.tv_id);
        btn_Attend = findViewById(R.id.btn_Attend);
        btn_Out = findViewById(R.id.btn_Out);
        btn_upload1 = findViewById(R.id.btn_upload1);

        Intent intent = getIntent();

        String userName = intent.getStringExtra("userName");
        String userID = intent.getStringExtra("userID");

        tv_id.setText(userName + "님 환영합니다.");

        //출석 체크로 가는 intent
        btn_Attend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent1 = new Intent(MainActivity.this, AttendActivity.class);
                intent1.putExtra("userName", userName);   //이름 넘기기
                intent1.putExtra("userID", userID);       //학번넘기기
                startActivity(intent1);
            }
        });

        //회원 탈퇴로 가는 intent
        btn_upload1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent2 = new Intent(MainActivity.this, ImgRegisterActivity.class);
                intent2.putExtra("userID", userID);
                startActivity(intent2);
            }
        });

        //회원 탈퇴로 가는 intent
        btn_Out.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent3 = new Intent(MainActivity.this, OutActivity.class);
                intent3.putExtra("userID", userID);
                startActivity(intent3);
            }
        });

    }





}