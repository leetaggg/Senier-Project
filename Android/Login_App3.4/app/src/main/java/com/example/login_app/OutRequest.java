package com.example.login_app;

import com.android.volley.AuthFailureError;
import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class OutRequest extends StringRequest {
    // 서버 URL 설정( PHP 파일 연동)
    final static private String URL = "http://39.124.26.132/login_App/Back_Out.php";
    private Map<String, String> map;
    public OutRequest(String userId, String userPassword, Response.Listener<String> listener) {
        super(Method.POST, URL, listener, null);

        map = new HashMap<>();
        map.put("userID", userId);
        map.put("userPassword", userPassword);

    }

    @Override
    protected Map<String, String> getParams() throws AuthFailureError {
        return map;
    }
}
