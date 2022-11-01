package com.example.login_app;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class AttendActivity extends AppCompatActivity {

    public TextView tv_stdName, tv_week1, tv_week2, tv_week3, tv_week4, tv_week5;
    private SwipeRefreshLayout swipeRefreshLayout;
    private SharedPreferences preferences;

    protected void onStart(){
        tv_stdName = findViewById(R.id.tv_stdName);
        tv_week1 = findViewById(R.id.tv_week1);
        tv_week2 = findViewById(R.id.tv_week2);
        tv_week3 = findViewById(R.id.tv_week3);
        tv_week4 = findViewById(R.id.tv_week4);
        tv_week5 = findViewById(R.id.tv_week5);

        //이름 설정정
        Intent intent = getIntent();
        String userName = intent.getStringExtra("userName");

        tv_stdName.setText(userName + "님의 출석표");

        String userID = intent.getStringExtra("userID");

        Response.Listener<String> responseListener = new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                try {
                    System.out.println("test" + response);
                    JSONObject jsonObject = new JSONObject(response);
                    boolean success = jsonObject.getBoolean("success");

                    if (success) { // 로그인에 성공한 경우
                        String one = jsonObject.getString("weekone");
                        String two = jsonObject.getString("weektwo");
                        String three = jsonObject.getString("weekthree");
                        String four = jsonObject.getString("weekfour");
                        String five = jsonObject.getString("weekfive");

                        if (one == "null"){
                            one = "결석";
                        }
                        if (two == "null"){
                            two = "결석";
                        }
                        if (three == "null"){
                            three = "결석";
                        }
                        if (four == "null"){
                            four = "결석";
                        }
                        if (five == "null"){
                            five = "결석";
                        }

                        tv_week1.setText(one);
                        tv_week2.setText(two);
                        tv_week3.setText(three);
                        tv_week4.setText(four);
                        tv_week5.setText(five);

                        Toast.makeText(getApplicationContext(),"갱신 되었습니다.",Toast.LENGTH_SHORT).show();

                    } else { // 로그인에 실패한 경우
                        Toast.makeText(getApplicationContext(),"갱신 실패",Toast.LENGTH_SHORT).show();
                        return;
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        };
        AttendRequest attendRequest = new AttendRequest(userID, responseListener);
        RequestQueue queue = Volley.newRequestQueue(AttendActivity.this);
        queue.add(attendRequest);

        super.onStart();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_attend);

        tv_stdName = findViewById(R.id.tv_stdName);
        tv_week1 = findViewById(R.id.tv_week1);
        tv_week2 = findViewById(R.id.tv_week2);
        tv_week3 = findViewById(R.id.tv_week3);
        tv_week4 = findViewById(R.id.tv_week4);
        tv_week5 = findViewById(R.id.tv_week5);

        //이름 설정정
       Intent intent = getIntent();
        String userName = intent.getStringExtra("userName");


        tv_stdName.setText(userName + "님의 출석표");

        swipeRefreshLayout = findViewById(R.id.swiperefreshlayout);
        swipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                /* swipe 시 진행할 동작 */
                String userID = intent.getStringExtra("userID");

                Response.Listener<String> responseListener = new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try {
                            System.out.println("test" + response);
                            JSONObject jsonObject = new JSONObject(response);
                            boolean success = jsonObject.getBoolean("success");

                            if (success) { // 로그인에 성공한 경우
                                String one = jsonObject.getString("weekone");
                                String two = jsonObject.getString("weektwo");
                                String three = jsonObject.getString("weekthree");
                                String four = jsonObject.getString("weekfour");
                                String five = jsonObject.getString("weekfive");

                                if (one == "null"){
                                    one = "결석";
                                }
                                if (two == "null"){
                                    two = "결석";
                                }
                                if (three == "null"){
                                    three = "결석";
                                }
                                if (four == "null"){
                                    four = "결석";
                                }
                                if (five == "null"){
                                    five = "결석";
                                }

                                tv_week1.setText(one);
                                tv_week2.setText(two);
                                tv_week3.setText(three);
                                tv_week4.setText(four);
                                tv_week5.setText(five);

                                Toast.makeText(getApplicationContext(),"갱신 되었습니다.",Toast.LENGTH_SHORT).show();

                            } else { // 로그인에 실패한 경우
                                Toast.makeText(getApplicationContext(),"갱신 실패",Toast.LENGTH_SHORT).show();
                                return;
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                };
                AttendRequest attendRequest = new AttendRequest(userID, responseListener);
                RequestQueue queue = Volley.newRequestQueue(AttendActivity.this);
                queue.add(attendRequest);


                /* 업데이트가 끝났음을 알림 */
                swipeRefreshLayout.setRefreshing(false);
            }
        });

    }

}