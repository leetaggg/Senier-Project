package com.example.login_app;

import android.Manifest;
import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import com.bumptech.glide.Glide;

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

public class ImgRegisterActivity extends Activity implements View.OnClickListener {
    //LOG
    private String TAGLOG = "ImgRegisterActivityLoG";

    //이미지 넣는 뷰와 업로드하기 위한 버튼
    private ImageView ivUploadImage1;
    private ImageView ivUploadImage2;
    private ImageView ivUploadImage3;
    private ImageView ivUploadImage4;
    private ImageView ivUploadImage5;
    private Button btnUploadImage, btn_goAround;

    public ArrayList<String> uploadFilePath = new ArrayList<String>();      //리스트 ["가", "나", "다"]
    public String uploadFileName;
    private int REQ_CODE_PICK_PICTURE1 = 1;
    private int REQ_CODE_PICK_PICTURE2 = 2;
    private int REQ_CODE_PICK_PICTURE3 = 3;
    private int REQ_CODE_PICK_PICTURE4 = 4;
    private int REQ_CODE_PICK_PICTURE5 = 5;

    //파일을 업로드 하기 위한 변수 선언
    private int serverResponseCode = 0;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_img_register);

        //외부 저장소에 권한 필요, 동적 퍼미션
        if(Build.VERSION.SDK_INT>= Build.VERSION_CODES.M){
            int permissionResult= checkSelfPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE);
            if(permissionResult== PackageManager.PERMISSION_DENIED){
                String[] permissions= new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE};
                requestPermissions(permissions,10);
            }
        }

        btn_goAround = findViewById(R.id.btn_goAround);
        btn_goAround.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(ImgRegisterActivity.this, LoginActivity.class);
                Activity activity = ImgRegisterActivity.this;   //뒤로가기 실패
                activity.finishAffinity();              //뒤로가기 실패
                startActivity(i);
            }
        });

        //변수 초기화
        InitVariable();
    }

    //초기화
    private void InitVariable() {
        //이미지를 넣을 뷰
        ivUploadImage1=(ImageView) findViewById(R.id.iv_upload_image1);
        ivUploadImage1.setOnClickListener(this);

        ivUploadImage2=(ImageView) findViewById(R.id.iv_upload_image2);
        ivUploadImage2.setOnClickListener(this);

        ivUploadImage3=(ImageView) findViewById(R.id.iv_upload_image3);
        ivUploadImage3.setOnClickListener(this);

        ivUploadImage4=(ImageView) findViewById(R.id.iv_upload_image4);
        ivUploadImage4.setOnClickListener(this);

        ivUploadImage5=(ImageView) findViewById(R.id.iv_upload_image5);
        ivUploadImage5.setOnClickListener(this);

        btnUploadImage = (Button) findViewById(R.id.btn_upload_image);
        btnUploadImage.setOnClickListener(this);
    }

    //==========================================사진을 불러오는 코드============================================================
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {

        Uri uri = data.getData();
        String path = getPath(uri);
        String name = getName(uri);

        if (resultCode == Activity.RESULT_OK) {
            if (requestCode == REQ_CODE_PICK_PICTURE1) {
                uploadFilePath.add(path);
                uploadFileName = name;        //이미지명
                Log.i(TAGLOG, "[onActivityResult] uploadFilePath:" + uploadFilePath + ", uploadFileName:" + uploadFileName);
                Bitmap bit = BitmapFactory.decodeFile(path);
                ivUploadImage1.setImageBitmap(bit);
                Glide.with(this).load(uri).into(ivUploadImage1);
            } else if (requestCode == REQ_CODE_PICK_PICTURE2) {
                uploadFilePath.add(path);
                uploadFileName = name;        //이미지명
                Log.i(TAGLOG, "[onActivityResult] uploadFilePath:" + uploadFilePath + ", uploadFileName:" + uploadFileName);
                Bitmap bit = BitmapFactory.decodeFile(path);
                ivUploadImage2.setImageBitmap(bit);
                Glide.with(this).load(uri).into(ivUploadImage2);
            } else if (requestCode == REQ_CODE_PICK_PICTURE3) {
                uploadFilePath.add(path);
                uploadFileName = name;        //이미지명
                Log.i(TAGLOG, "[onActivityResult] uploadFilePath:" + uploadFilePath + ", uploadFileName:" + uploadFileName);
                Bitmap bit = BitmapFactory.decodeFile(path);
                ivUploadImage3.setImageBitmap(bit);
                Glide.with(this).load(uri).into(ivUploadImage3);
            } else if (requestCode == REQ_CODE_PICK_PICTURE4) {
                uploadFilePath.add(path);
                uploadFileName = name;        //이미지명
                Log.i(TAGLOG, "[onActivityResult] uploadFilePath:" + uploadFilePath + ", uploadFileName:" + uploadFileName);
                Bitmap bit = BitmapFactory.decodeFile(path);
                ivUploadImage4.setImageBitmap(bit);
                Glide.with(this).load(uri).into(ivUploadImage4);
            } else if (requestCode == REQ_CODE_PICK_PICTURE5) {
                uploadFilePath.add(path);
                uploadFileName = name;        //이미지명
                Log.i(TAGLOG, "[onActivityResult] uploadFilePath:" + uploadFilePath + ", uploadFileName:" + uploadFileName);
                Bitmap bit = BitmapFactory.decodeFile(path);
                ivUploadImage5.setImageBitmap(bit);
                Glide.with(this).load(uri).into(ivUploadImage5);
            }
        }
    }


    //실제 경로 찾기
    private String getPath(Uri uri) {
        String[] projection = {MediaStore.Images.Media.DATA};
        Cursor cursor = managedQuery(uri, projection, null, null, null);
        int column_index = cursor.getColumnIndexOrThrow(MediaStore.Images.Media.DATA);
        cursor.moveToFirst();
        return cursor.getString(column_index);
    }
    //파일명 찾기기
    private String getName(Uri uri) {
        String[] projection = {MediaStore.Images.ImageColumns.DISPLAY_NAME};
        Cursor cursor = managedQuery(uri, projection, null, null, null);
        int column_index = cursor.getColumnIndexOrThrow(MediaStore.Images.ImageColumns.DISPLAY_NAME);
        cursor.moveToFirst();
        return cursor.getString(column_index);
    }

    // uri 아이디 찾기
    private String getUriId(Uri uri) {
        String[] projection = {MediaStore.Images.ImageColumns._ID};
        Cursor cursor = managedQuery(uri, projection, null, null, null);
        int column_index = cursor.getColumnIndexOrThrow(MediaStore.Images.ImageColumns._ID);
        cursor.moveToFirst();
        return cursor.getString(column_index);
    }

    // ============================== 사진을 서버에 전송하기 위한 스레드 ========================

    private class UploadImageToServer extends AsyncTask<String, String, String> {
        ProgressDialog mProgressDialog;
        String fileName = null;
        HttpURLConnection conn = null;
        DataOutputStream dos = null;
        String lineEnd = "\r\n";
        String twoHyphens = "--";
        String boundary = "*****";
        int bytesRead, bytesAvailable, bufferSize;
        byte[] buffer;
        int maxBufferSize = 10 * 10240 * 10240;
        File sourceFile = null;

        @Override
        protected void onPreExecute() {
            // Create a progressdialog
            mProgressDialog = new ProgressDialog(ImgRegisterActivity.this);
            mProgressDialog.setTitle("Loading...");
            mProgressDialog.setMessage("Image uploading...");
            mProgressDialog.setCanceledOnTouchOutside(false);
            mProgressDialog.setIndeterminate(false);
            mProgressDialog.show();
        }

        @Override
        protected String doInBackground(String... serverUrl) {
            Intent intent = getIntent();
            String userID = intent.getStringExtra("userID");
            for(int i = 0; i < uploadFilePath.size(); i++) {
                fileName = uploadFilePath.get(i);
                sourceFile = new File(uploadFilePath.get(i));
                if (!sourceFile.isFile()) {
                    runOnUiThread(new Runnable() {
                        public void run() {
                            Log.i(TAGLOG, "[UploadImageToServer] Source File not exist :" + uploadFilePath);
                        }
                    });
                    return null;
                } else {
                    try {
                        // open a URL connection to the Servlet
                        FileInputStream fileInputStream = new FileInputStream(sourceFile);
                        URL url = new URL(serverUrl[0]);


                        // Open a HTTP  connection to  the URL
                        conn = (HttpURLConnection) url.openConnection();
                        conn.setDoInput(true); // Allow Inputs
                        conn.setDoOutput(true); // Allow Outputs
                        conn.setUseCaches(false); // Don't use a Cached Copy
                        conn.setRequestMethod("POST");
                        conn.setRequestProperty("Connection", "Keep-Alive");
                        conn.setRequestProperty("ENCTYPE", "multipart/form-data");
                        conn.setRequestProperty("Content-Type", "multipart/form-data;boundary=" + boundary);
                        conn.setRequestProperty("uploaded_file", fileName);
                        Log.i(TAGLOG, "fileName: " + fileName);

                        dos = new DataOutputStream(conn.getOutputStream());

                        // 사용자 이름으로 폴더를 생성하기 위해 사용자 이름을 서버로 전송한다.
                        dos.writeBytes(twoHyphens + boundary + lineEnd);
                        dos.writeBytes("Content-Disposition: form-data; name=\"data1\"" + lineEnd);
                        dos.writeBytes(lineEnd);

                        dos.writeBytes(userID);     //폴더명 정하기.
                        dos.writeBytes(lineEnd);

                        String no = String.format("%03d", (i+1));

                        // 이미지 전송
                        dos.writeBytes(twoHyphens + boundary + lineEnd);
                        String number = no +".jpg";
                        dos.writeBytes("Content-Disposition: form-data; name=\"uploaded_file\"; filename=\"" + userID + '_' + number + "\"" + lineEnd);
                        dos.writeBytes(lineEnd);

                        // create a buffer of  maximum size
                        bytesAvailable = fileInputStream.available();
                        bufferSize = Math.min(bytesAvailable, maxBufferSize);
                        buffer = new byte[bufferSize];

                        // read file and write it into form...
                        bytesRead = fileInputStream.read(buffer, 0, bufferSize);
                        while (bytesRead > 0) {
                            dos.write(buffer, 0, bufferSize);
                            bytesAvailable = fileInputStream.available();
                            bufferSize = Math.min(bytesAvailable, maxBufferSize);
                            bytesRead = fileInputStream.read(buffer, 0, bufferSize);
                        }

                        // send multipart form data necesssary after file data...
                        dos.writeBytes(lineEnd);
                        dos.writeBytes(twoHyphens + boundary + twoHyphens + lineEnd);

                        // Responses from the server (code and message)
                        serverResponseCode = conn.getResponseCode();
                        String serverResponseMessage = conn.getResponseMessage();

                        Log.i(TAGLOG, "[UploadImageToServer] HTTP Response is : " + serverResponseMessage + ": " + serverResponseCode);

                        if (serverResponseCode == 200) {
                            runOnUiThread(new Runnable() {
                                public void run() {
                                    Toast.makeText(ImgRegisterActivity.this, "이미지 업로드 완료", Toast.LENGTH_SHORT).show();
                                }
                            });
                        }
                        //close the streams //
                        fileInputStream.close();
                        dos.flush();
                        dos.close();

                    } catch (MalformedURLException ex) {
                        ex.printStackTrace();
                        runOnUiThread(new Runnable() {
                            public void run() {
                                Toast.makeText(ImgRegisterActivity.this, "MalformedURLException", Toast.LENGTH_SHORT).show();
                            }
                        });
                        Log.i(TAGLOG, "[UploadImageToServer] error: " + ex.getMessage(), ex);
                    } catch (Exception e) {
                        e.printStackTrace();
                        runOnUiThread(new Runnable() {
                            public void run() {
                                Toast.makeText(ImgRegisterActivity.this, "Got Exception : see logcat ", Toast.LENGTH_SHORT).show();
                            }
                        });
                        Log.i(TAGLOG, "[UploadImageToServer] Upload file to server Exception Exception : " + e.getMessage(), e);
                    }
                    Log.i(TAGLOG, "[UploadImageToServer] Finish");
                } // End else block
            }
            return null;
        }

        @Override
        protected void onPostExecute (String s){
            mProgressDialog.dismiss();
        }
    }
    // ==========================================================================================

    @Override
    public void onClick(View v) {
        Intent i = new Intent(Intent.ACTION_PICK);
        switch (v.getId()) {
            case R.id.iv_upload_image1:
                i.setType(MediaStore.Images.Media.CONTENT_TYPE);
                i.setData(MediaStore.Images.Media.EXTERNAL_CONTENT_URI); // images on the SD card.

                // 결과를 리턴하는 Activity 호출
                startActivityForResult(i, REQ_CODE_PICK_PICTURE1);
                break;

            case R.id.iv_upload_image2:
                i.setType(MediaStore.Images.Media.CONTENT_TYPE);
                i.setData(MediaStore.Images.Media.EXTERNAL_CONTENT_URI); // images on the SD card.

                // 결과를 리턴하는 Activity 호출
                startActivityForResult(i, REQ_CODE_PICK_PICTURE2);
                break;

            case R.id.iv_upload_image3:
                i.setType(MediaStore.Images.Media.CONTENT_TYPE);
                i.setData(MediaStore.Images.Media.EXTERNAL_CONTENT_URI); // images on the SD card.

                // 결과를 리턴하는 Activity 호출
                startActivityForResult(i, REQ_CODE_PICK_PICTURE3);
                break;

            case R.id.iv_upload_image4:
                i.setType(MediaStore.Images.Media.CONTENT_TYPE);
                i.setData(MediaStore.Images.Media.EXTERNAL_CONTENT_URI); // images on the SD card.

                // 결과를 리턴하는 Activity 호출
                startActivityForResult(i, REQ_CODE_PICK_PICTURE4);
                break;

            case R.id.iv_upload_image5:
                i.setType(MediaStore.Images.Media.CONTENT_TYPE);
                i.setData(MediaStore.Images.Media.EXTERNAL_CONTENT_URI); // images on the SD card.

                // 결과를 리턴하는 Activity 호출
                startActivityForResult(i, REQ_CODE_PICK_PICTURE5);
                break;

            case R.id.btn_upload_image:
                if (uploadFilePath != null) {
                    UploadImageToServer uploadimagetoserver = new UploadImageToServer();
                    uploadimagetoserver.execute("http://39.124.26.132/login_App/ImageUploadToServer.php");
                } else {
                    Toast.makeText(ImgRegisterActivity.this, "이미지가 다 삽입되지 않았습니다.", Toast.LENGTH_SHORT).show();
                }
                break;
        }
    }
}