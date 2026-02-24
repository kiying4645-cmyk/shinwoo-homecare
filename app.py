import streamlit as st
import base64
from pathlib import Path

# 페이지 설정
st.set_page_config(
    page_title="신우홈케어 - 프리미엄 홈케어 솔루션",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 로드 함수
def local_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 이미지 Base64 변환 (로컬 이미지 표시용)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 경로 설정
current_dir = Path(__file__).parent
css_path = current_dir / "style.css"
assets_dir = current_dir / "assets"
sink_img_path = assets_dir / "service_sink.png"
logo_path = assets_dir / "logo.png"

# CSS 적용
if css_path.exists():
    local_css(css_path)

# 메인 레이아웃
def main():
    # 로고 표시
    if logo_path.exists():
        st.image(str(logo_path), width=200)

    # 헤더 섹션
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">SHINWOO HOMECARE</h1>
            <p class="hero-subtitle">전문가의 손길로 완성하는 주방과 욕실의 혁신</p>
            <p style="color: #666;">신뢰와 정성으로 보답하는 신우홈케어입니다.</p>
        </div>
    """, unsafe_allow_html=True)

    # 서비스 소개 섹션
    st.markdown("<h2 style='text-align: center; margin-bottom: 50px;'>OUR SERVICES</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="service-card">
                <div class="service-icon">🚰</div>
                <h3>수전 및 싱크대</h3>
                <p>프리미엄 수전 교체 및 싱크대 설치를 전문적으로 진행합니다.</p>
            </div>
        """, unsafe_allow_html=True)
        if sink_img_path.exists():
            st.image(str(sink_img_path), use_container_width=True)

    with col2:
        st.markdown("""
            <div class="service-card">
                <div class="service-icon">🛠️</div>
                <h3>배수관 수리</h3>
                <p>노후된 배수관 교체 및 막힘 문제를 신속하게 해결해 드립니다.</p>
            </div>
        """, unsafe_allow_html=True)
        # 이미지 추가 예정

    with col3:
        st.markdown("""
            <div class="service-card">
                <div class="service-icon">🛡️</div>
                <h3>종합 보수</h3>
                <p>생활의 불편함을 덜어드리는 꼼꼼한 홈케어 서비스를 제공합니다.</p>
            </div>
        """, unsafe_allow_html=True)

    # 신뢰 섹션
    st.markdown("---")
    st.markdown("""
        <div style="padding: 50px; background-color: white; border-radius: 20px; text-align: center;">
            <h2 style="color: #2c3e50;">고객이 신뢰하는 이유</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 30px;">
                <div style="flex: 1; min-width: 200px; padding: 20px;">
                    <h4>✅ 전문가 시공</h4>
                    <p>수년간의 노하우를 가진 대표가 직접 현장을 관리합니다.</p>
                </div>
                <div style="flex: 1; min-width: 200px; padding: 20px;">
                    <h4>✅ 정직한 견적</h4>
                    <p>과잉 시공 없이 정직하고 투명한 가격을 약속합니다.</p>
                </div>
                <div style="flex: 1; min-width: 200px; padding: 20px;">
                    <h4>✅ 책임 A/S</h4>
                    <p>시공 후 발생할 수 있는 문제까지 책임지고 관리합니다.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 하단 정보 및 플로팅 버튼
    st.markdown(f"""
        <div class="contact-bar">
            <a href="tel:010-9319-7887" class="floating-btn">
                📞 전화문의 (대표 김태건)
            </a>
            <a href="#" class="floating-btn kakao">
                💬 카카오톡 견적문의
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    # 풋터
    st.markdown("---")
    st.markdown(f"""
        <div style="text-align: center; color: #888; padding: 20px;">
            <p>상호: 신우홈케어 | 대표: 김태건 | 연락처: 010-9319-7887</p>
            <p>© 2026 SHINWOO HOMECARE. All rights reserved.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
