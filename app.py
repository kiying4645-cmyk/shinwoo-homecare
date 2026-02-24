import streamlit as st
import base64
from pathlib import Path

# 페이지 설정
st.set_page_config(
    page_title="신우홈케어 | 수전 및 싱크대 전문 프리미엄 홈케어",
    page_icon="✨",
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
hero_img_path = assets_dir / "hero_faucet.png"
tools_img_path = assets_dir / "pro_tools.png"
logo_path = assets_dir / "logo_transparent.png"

# CSS 적용
if css_path.exists():
    local_css(css_path)

def main():
    # 상단 헤더
    logo_html = ""
    if logo_path.exists():
        logo_base64 = get_base64_of_bin_file(str(logo_path))
        logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="height: 50px;">'
    else:
        logo_html = 'SHINWOO<span style="color:#2980B9">.</span>'

    st.markdown(f"""
        <div class="premium-header">
            <div class="header-logo">{logo_html}</div>
            <div style="display: flex; gap: 40px; font-weight: 500; font-size: 0.85rem; color: #666;">
                <span>SERVICES</span>
                <span>PROJECTS</span>
                <span>ABOUT</span>
                <span style="color: #1A2B3C; font-weight: 700;">010-9319-7887</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 히어로 섹션
    if hero_img_path.exists():
        hero_base64 = get_base64_of_bin_file(str(hero_img_path))
        st.markdown(f"""
            <div class="hero-wrapper">
                <img src="data:image/png;base64,{hero_base64}" class="hero-img" alt="Luxury Faucet">
                <div class="hero-overlay"></div>
                <div class="hero-content">
                    <span style="color: #2980B9; font-weight: 700; letter-spacing: 2px;">PREMIUM HOME CARE</span>
                    <h1 class="hero-title">주방의 품격을 완성하는<br>섬세한 전문가의 손길.</h1>
                    <p class="hero-desc">
                        신우홈케어는 최상급 수전 설치와 싱크대 수리 분야의 압도적인 기술력을 바탕으로, 
                        고객님의 공간을 단순한 기능 이상의 예술로 완성합니다.
                    </p>
                    <a href="tel:010-9319-7887" class="btn-cta" style="background:#1A2B3C; color:white; padding: 20px 45px; border-radius:4px; text-decoration:none; font-weight:600; display:inline-block;">견적 상담 신청</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # 서비스 섹션
    st.markdown('<h2 class="section-title">Professional Services</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="service-container">
            <div class="pro-card">
                <div class="card-icon">01</div>
                <h3 style="font-size: 1.5rem; margin-bottom: 20px;">수전 및 싱크대 설치</h3>
                <p style="color: #6C757D; line-height: 1.8;">글로벌 하이엔드 수전 및 싱크대 솔루션을 제공합니다. 빈틈없는 완벽한 마감과 유려한 디자인을 경험하세요.</p>
            </div>
            <div class="pro-card">
                <div class="card-icon">02</div>
                <h3 style="font-size: 1.5rem; margin-bottom: 20px;">배수 시스템 최적화</h3>
                <p style="color: #6C757D; line-height: 1.8;">노후된 배수관을 교체하고 첨단 기술을 활용해 막힘과 악취 문제를 근본적으로 해결합니다.</p>
            </div>
            <div class="pro-card">
                <div class="card-icon">03</div>
                <h3 style="font-size: 1.5rem; margin-bottom: 20px;">대표 김태건 책임 시공</h3>
                <p style="color: #6C757D; line-height: 1.8;">하청 업체에 맡기지 않습니다. 대표가 직접 모든 현장을 방문하여 정직하고 투명한 시공을 약속합니다.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 도구 및 기술 섹션
    if tools_img_path.exists():
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.image(str(tools_img_path), use_container_width=True)
        with col2:
            st.markdown("""
                <div style="padding: 60px 20px;">
                    <h2 style="font-size: 2.5rem; color: #1A2B3C;">최고의 결과는<br>정밀한 도구에서 나옵니다.</h2>
                    <p style="margin-top: 30px; color: #6C757D; line-height: 2;">
                        신우홈케어는 시공의 완성도를 높이기 위해 항상 최상의 장비만을 사용합니다. 
                        섬세한 작업이 필요한 배수관 연결부터 누수 방지 마감까지, 전용 도구를 사용한 
                        정밀한 시공으로 시공 후 발생할 수 있는 소음과 누수 위험을 최소화합니다.
                    </p>
                </div>
            """, unsafe_allow_html=True)

    # 하단 트러스트 바
    st.markdown("""
        <div class="trust-bar">
            <div>
                <h4 style="font-size: 2rem; margin-bottom: 10px;">1,200+</h4>
                <p style="color: #AAA;">누적 시공 건수</p>
            </div>
            <div>
                <h4 style="font-size: 2rem; margin-bottom: 10px;">99%</h4>
                <p style="color: #AAA;">고객 만족도</p>
            </div>
            <div>
                <h4 style="font-size: 2rem; margin-bottom: 10px;">24hr</h4>
                <p style="color: #AAA;">긴급 상담 대응</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 플로팅 버튼 (전화 및 카톡)
    st.markdown("""
        <a href="tel:010-9319-7887" class="bottom-cta">
            📞 실시간 전화 문의
        </a>
    """, unsafe_allow_html=True)

    # 풋터
    st.markdown(f"""
        <div style="padding: 100px 10%; background: #F8F9FA; color: #444; font-size: 0.9rem;">
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div>
                    <h3 style="font-size: 1.5rem; color: #1A2B3C; margin-bottom: 20px;">SHINWOO HOMECARE</h3>
                    <p>대표: 김태건 | 상호: 신우홈케어</p>
                    <p>연락처: 010-9319-7887</p>
                </div>
                <div style="text-align: right;">
                    <p>© 2026 SHINWOO HOMECARE. All rights reserved.</p>
                    <p style="margin-top: 10px; color: #BBB;">Cleanliness. Precision. Trust.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
