package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Spring Boot가 시작되는 곳.
 * 이 main을 실행하면 내장 웹 서버가 뜨고, demo 패키지 아래의
 * 컨트롤러, 서비스, DB 설정을 자동으로 찾아서 연결한다.
 */
@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

}
