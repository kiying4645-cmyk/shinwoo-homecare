import streamlit as st
import base64
from pathlib import Path

# 페이지 설정
st.set_page_config(
    page_title="신우홈케어 | Anti-gravity Premium Homecare",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 로드 함수
def local_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 이미지 Base64 변환
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 경로 설정
current_dir = Path(__file__).parent
css_path = current_dir / "style.css"
assets_dir = current_dir / "assets"
logo_path = assets_dir / "logo.png"
bg_path = assets_dir / "bg_futuristic.png"
sink_img_path = assets_dir / "service_sink.png"

# CSS 적용
if css_path.exists():
    local_css(css_path)

# 배경 오버레이 설정
if bg_path.exists():
    bg_base64 = get_base64_of_bin_file(str(bg_path))
    st.markdown(f"""
        <div class="bg-overlay" style="background-image: url('data:image/png;base64,{bg_base64}');"></div>
    """, unsafe_allow_html=True)

def main():
    # 투명 헤더 (네비게이션 스타일)
    st.markdown(f"""
        <div class="sticky-header">
            <div style="font-weight: 800; font-size: 1.5rem; letter-spacing: -1px;">SHINWOO</div>
            <div style="display: flex; gap: 30px; font-weight: 300; font-size: 0.9rem;">
                <span>SERVICES</span>
                <span>ABOUT</span>
                <span>CONTACT</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 히어로 섹션
    st.markdown("""
        <div class="hero-sec main-container">
            <h1 class="hero-headline">WEIGHTLESS<br>HOMECARE.</h1>
            <p class="hero-subtext">
                신우홈케어는 단순한 수리를 넘어, 주방과 욕실의 혁신을 제안합니다. 
                차원이 다른 섬세함으로 집안의 모든 중력을 덜어내겠습니다.
            </p>
            <div style="margin-top: 50px;">
                <a href="tel:010-9319-7887" class="btn-primary">실시간 견적 상담 →</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 서비스 그리드 (비대칭 레이아웃)
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 2.5rem; font-weight: 700; margin-top: 100px;'>PREMIUM SOLUTIONS</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="service-grid">
            <div class="service-card-new card-1">
                <span style="color: #007BFF; font-weight: 800;">01</span>
                <h3 style="font-size: 1.8rem; margin-top: 20px;">수전 및 싱크대 설치</h3>
                <p style="color: #A0A0A0; margin-top: 15px;">글로벌 하이엔드 수전 및 싱크대 솔루션을 제공합니다. 빈틈없는 완벽한 마감과 유려한 디자인을 경험하세요.</p>
            </div>
            <div class="service-card-new card-2">
                <span style="color: #007BFF; font-weight: 800;">02</span>
                <h3 style="font-size: 1.8rem; margin-top: 20px;">배수 시스템 최적화</h3>
                <p style="color: #A0A0A0; margin-top: 15px;">노후된 배수관을 교체하고 첨단 기술을 활용해 막힘과 악취 문제를 근본적으로 해결합니다.</p>
            </div>
            <div class="service-card-new card-3">
                <span style="color: #007BFF; font-weight: 800;">03</span>
                <h3 style="font-size: 1.8rem; margin-top: 20px;">미세한 누수 탐지</h3>
                <p style="color: #A0A0A0; margin-top: 15px;">보이지 않는 미세한 누수까지 정밀하게 탐지하여 효율적인 보강 작업을 수행합니다.</p>
            </div>
            <div class="service-card-new card-4">
                <span style="color: #007BFF; font-weight: 800;">04</span>
                <h3 style="font-size: 1.8rem; margin-top: 20px;">대표 김태건 직영 서비스</h3>
                <p style="color: #A0A0A0; margin-top: 15px;">모든 현장은 다년간의 노하우를 가진 대표가 직접 설계하고 시공하여 신뢰를 보장합니다.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 모바일 전용 문의바 (하단 탭바 스타일)
    st.markdown("""
        <div class="contact-bar-mobile">
            <a href="tel:010-9319-7887" style="color: white; text-decoration: none; text-align: center;">
                <div style="font-size: 1.2rem;">📞</div>
                <div style="font-size: 0.7rem; color: #A0A0A0;">CALL</div>
            </a>
            <a href="#" style="color: white; text-decoration: none; text-align: center;">
                <div style="font-size: 1.2rem;">💬</div>
                <div style="font-size: 0.7rem; color: #A0A0A0;">KAKAOTALK</div>
            </a>
            <div style="text-align: center;">
                <div style="font-size: 1.2rem; color: #007BFF;">🏠</div>
                <div style="font-size: 0.7rem; color: #007BFF;">HOME</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 풋터
    st.markdown(f"""
        <div style="text-align: left; padding: 100px 0 50px; border-top: 0.5pt solid rgba(255,255,255,0.1); margin-top: 150px;">
            <div style="font-weight: 800; font-size: 1.5rem; margin-bottom: 20px;">SHINWOO HOMECARE</div>
            <div style="display: flex; gap: 50px; flex-wrap: wrap; color: #666; font-size: 0.8rem;">
                <div>
                    <div style="font-weight: 600; color: #AAA; margin-bottom: 10px;">CONTACT</div>
                    <p>010-9319-7887 (김태건)</p>
                </div>
                <div>
                    <div style="font-weight: 600; color: #AAA; margin-bottom: 10px;">LEGAL</div>
                    <p>상호: 신우홈케어 | 대표: 김태건</p>
                </div>
                <div style="flex-grow: 1; text-align: right;">
                    <p>© 2026 SHINWOO. DESIGNED BY ANTI-GRAVITY.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
