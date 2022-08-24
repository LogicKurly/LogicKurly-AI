## 📂 Data Collection 
### 1. 데이터 개요 
#### [식품의약안전처 조리식품 레시피 DB 데이터](http://www.foodsafetykorea.go.kr/api/openApiInfo.do?menu_grp=MENU_GRP31&menu_no=661&show_cnt=10&start_idx=1&svc_no=COOKRCP01)
- 1358개 레시피에 사용되는 식재료 상위 25가지 추출
 

### 2. 데이터 수집 및 전처리 방법 

#### 1. [AI Hub - 농산물 품질(QC) 이미지](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100)
#### 2. [FoodiesFeed - 웹 크롤링](https://www.foodiesfeed.com/)
- 각 카테고리 별로 무료 이미지 사이트인 FoodiesFeed 에서 이미지 크롤링 
- 크롤링한 이미지에서 '카테고리에 해당하지 않는 이미지' 등을 제거
- 이미지에 대하여 Annotation tool을 사용하여, bounding box annotation 진행
- bounding box 형태는 COCO format을 따름
