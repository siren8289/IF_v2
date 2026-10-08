
package com.example.demo.global.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

import java.time.Duration;

/**
 * IF_v2 애플리케이션 공통 설정.
 *
 * [역할]
 * 1. Spring Boot → FastAPI HTTP 통신 객체 생성
 * 2. Swagger/OpenAPI 문서 설정
 *
 * 기존 RestTemplateConfig와 SwaggerConfig를 통합한다.
 */
@Configuration
public class AppConfig {

    /**
     * FastAPI 호출용 RestTemplate Bean.
     *
     * [처리 흐름]
     * AIClient → RestTemplate → FastAPI
     *
     * 연결 및 응답 제한 시간을 설정해
     * 외부 AI 서버 장애가 Spring 요청을 무기한 점유하지 않도록 한다.
     *
     * 주의: 3초 제한은 NFR 목표를 자동 보장하지 않는다.
     */
    @Bean
    public RestTemplate restTemplate(RestTemplateBuilder builder) {
        return builder
                .setConnectTimeout(Duration.ofSeconds(3))
                .setReadTimeout(Duration.ofSeconds(3))
                .build();
    }

    /**
     * Swagger API 문서의 기본 정보.
     *
     * Spring Controller의 엔드포인트를
     * OpenAPI 문서로 확인할 수 있도록 설정한다.
     */
    @Bean
    public OpenAPI ifOpenApi() {
        return new OpenAPI()
                .info(new Info()
                        .title("IF Risk Assessment API")
                        .version("0.3.0")
                        .description(
                                "IF_v2 신청자·일자리·위험도 평가 API"
                        ));
    }
}
