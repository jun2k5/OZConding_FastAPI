from fastapi import APIRouter

from meetifyr.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"], redirect_slashes=False)
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)

#원래는 어떤 db를 사용하는지 url에 적을 필요가 없다.
#강의에서만 이렇게 한다.
#실전에서는 db이름을 url에 넣지말 것.


@edgedb_router.post(
        "",
        description="meeting 을 생성합니다.",
        )
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")

# 왜 Dict가 아닌 DTO(Data Transfer Object)를 사용하는가? 
# 1.클라이언트단에서 받은 데이터의 값이 필수값인지 Optional한 값인지 알 수 없다.
# 2.추가 필드가 있는지 알 수 없다.
# 3.서버단에서 실수로 key를 누락하거나 추가해도 오류를 잡기 어렵다.

@mysql_router.post(
        "",
        description="meeting 을 생성합니다.",
        )
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")






