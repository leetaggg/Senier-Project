package com.example.login_app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class OutActivity extends AppCompatActivity {

    public TextView tv_Out;
    public EditText et_OutPass;
    public Button btn_ExOut;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_out);

        tv_Out = findViewById(R.id.tv_Out);
        et_OutPass = findViewById(R.id.et_OutPass);
        btn_ExOut = findViewById(R.id.btn_ExOut);

        btn_ExOut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //editText에서 값 받아오기
                Intent intent = getIntent();
                String userID = intent.getStringExtra("userID");
                String userPass = et_OutPass.getText().toString();

                //editText 초기화
                et_OutPass.setText("");


                Response.Listener<String> responseListener = new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try {
                            System.out.println("test" + response);
                            JSONObject jsonObject = new JSONObject(response);
                            boolean success = jsonObject.getBoolean("success");
                            if (success) { // 로그인에 성공한 경우
                                Toast.makeText(getApplicationContext(),"success",Toast.LENGTH_SHORT).show();
                                Intent intent = new Intent(OutActivity.this, LoginActivity.class);
                                Activity activity = OutActivity.this;   //뒤로가기 실패
                                activity.finishAffinity();              //뒤로가기 실패
                                startActivity(intent);                  //로그인 화면으로 가기

                            } else { // 로그인에 실패한 경우
                                Toast.makeText(getApplicationContext(),"비밀번호를 다시 입력하세요",Toast.LENGTH_SHORT).show();
                                return;
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                };
                OutRequest outRequest = new OutRequest(userID, userPass, responseListener);
                RequestQueue queue = Volley.newRequestQueue(OutActivity.this);
                queue.add(outRequest);

            }
        });
    }

}