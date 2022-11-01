package com.example.login_app;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class LoginActivity extends AppCompatActivity {
    private EditText et_id1, et_pass2;
    private Button btn_login, btn_register;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        et_id1 = findViewById(R.id.et_id1);
        et_pass2 = findViewById(R.id.et_pass2);
        btn_login = findViewById(R.id.btn_login);
        btn_register = findViewById(R.id.btn_register);


        // 회원가입 버튼을 클릭 시 수행
        btn_register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(LoginActivity.this, RegisterActivity.class);
                startActivity(intent);
            }
        });

        btn_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // EditText에 현재 입력되어있는 값을 get(가져온다)해온다.
                String userID = et_id1.getText().toString();
                String userPassword = et_pass2.getText().toString();

                //로그인 정보지우기
                et_id1.setText("");
                et_pass2.setText("");

                Toast.makeText(getApplicationContext(),"로그인 시도중",Toast.LENGTH_SHORT).show();

                Response.Listener<String> responseListener = new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try {
                            System.out.println("student" + response);
                            JSONObject jsonObject = new JSONObject(response);
                            int success = jsonObject.getInt("success");


                            if (success == 1) { //로그인 성공 사진 등록 안됨 (사진 등록 + 처음 사진 등록 한다 문구)
                                AlertDialog.Builder builder = new AlertDialog.Builder(LoginActivity.this);
                                builder.setTitle("로그인 오류");                       //제목 부분
                                builder.setMessage("사진을 전송 하시겠습니까?");               //내용 부분
                                builder.setPositiveButton("예", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialogInterface, int i) {

                                        Intent intent2 = new Intent(LoginActivity.this, ImgRegisterActivity.class);
                                        intent2.putExtra("userID", userID);
                                        startActivity(intent2);

                                    }
                                });
                                builder.setNegativeButton("아니오", null);
                                builder.create().show();

                            } else if(success == 2) {   //로그인 성공 사진 등록은 됐는데 PC에서 유사도 측정 안함(기달려 달라 문구)
                                AlertDialog.Builder builder = new AlertDialog.Builder(LoginActivity.this);
                                builder.setTitle("로그인 오류");                       //제목 부분
                                builder.setMessage("대기해주세요");               //내용 부분
                                builder.setPositiveButton("예", null);
                                builder.create().show();

                            } else if(success == 3) {   //로그인 성공 사진 등록은 됐는데 PC에서 유사도 측정 실패(사진 등록 + 다시 해달라 문구)
                                AlertDialog.Builder builder = new AlertDialog.Builder(LoginActivity.this);
                                builder.setTitle("로그인 오류");                       //제목 부분
                                builder.setMessage("유사도측정 실패\n 사진을 다시 전송해주세요.");               //내용 부분
                                builder.setPositiveButton("예", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialogInterface, int i) {

                                        Intent intent2 = new Intent(LoginActivity.this, ImgRegisterActivity.class);
                                        intent2.putExtra("userID", userID);
                                        startActivity(intent2);

                                    }
                                });
                                builder.setNegativeButton("아니오", null);
                                builder.create().show();

                            } else if(success == 4) {   //로그인 성공 사진 등록은 됐는데 PC에서 유사도 측정 성공(이제 출석확인 화면)
                                String userID = jsonObject.getString("userID");
                                String userPass = jsonObject.getString("userPassword");
                                String userName = jsonObject.getString("name");


                                //메인으로 가는 intent
                                Toast.makeText(getApplicationContext(), "로그인에 성공하였습니다.", Toast.LENGTH_SHORT).show();
                                Intent intent = new Intent(LoginActivity.this, MainActivity.class);
                                intent.putExtra("userID", userID);
                                intent.putExtra("userPass", userPass);
                                intent.putExtra("userName", userName);

                                startActivity(intent);

                            }
                            else { // 아이디 비밀번호가 틀렸을 경우 0
                                Toast.makeText(getApplicationContext(),"비밀번호가 틀렸습니다.",Toast.LENGTH_SHORT).show();
                                return;
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                };
                LoginRequest loginRequest = new LoginRequest(userID, userPassword, responseListener);
                RequestQueue queue = Volley.newRequestQueue(LoginActivity.this);
                queue.add(loginRequest);
            }
        });
    }

}