
package com.example.demo.global.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * IF_v2 웹 요청 공통 설정.
 *
 * [역할]
 * - React 프론트엔드의 Spring API 접근 허용
 * - 허용 출처, HTTP 메서드, 요청 헤더 관리
 *
 * [통신 흐름]
 * React(Vite) → Spring Boot(/api/**)
 *
 * 운영 환경에서는 허용 출처를 실제 도메인으로 제한한다.
 */
@Configuration
public class WebConfig implements WebMvcConfigurer {

    /**
     * 접근을 허용할 프론트엔드 주소.
     *
     * application.yml 또는 환경변수에서 재설정 가능.
     * 기본값은 로컬 개발 환경 기준이다.
     */
    @Value("${app.cors.allowed-origins:http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000}")
    private String[] allowedOrigins;

    /**
     * /api/** 요청에 대한 CORS 정책.
     *
     * OPTIONS 프리플라이트 요청을 포함하여
     * 지정한 출처의 HTTP 요청을 허용한다.
     */
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins(allowedOrigins)
                .allowedMethods(
                        "GET", "POST", "PUT",
                        "PATCH", "DELETE", "OPTIONS"
                )
                .allowedHeaders("*")
                .allowCredentials(true)
                .maxAge(3600);
    }
}
