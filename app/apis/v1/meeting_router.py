from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)
# 원래는 어떤 db를 사용하는지 url에 적지 말기


@mysql_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:

    return CreateMeetingResponse(url_code="abc")
    # dict로 안 주고 CreateMeetingResponse이런형식을 사용해야하는 이유
    # Swagger에서 try it out 하기전 어떤 형식의 데이터인지 확인 불가
