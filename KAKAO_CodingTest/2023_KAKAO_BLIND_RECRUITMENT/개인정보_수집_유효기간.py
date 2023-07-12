# 2023 KAKAO BLIND RECRUITMENT 개인정보 수집 유효기간 (LV.1)
def solution(today, terms, privacies):
    def get_expired_date(YYYY_MM_DD: str, months: int):
        YYYY, MM, DD = map(int, YYYY_MM_DD.split('.'))
        MM += months
        while MM > 12:
            YYYY, MM = YYYY + 1, MM - 12
        DD = DD - 1
        YYYY = str(YYYY)
        MM = str(MM) if MM >= 10 else '0' + str(MM)
        DD = str(DD) if DD >= 10 else '0' + str(DD)
        return '.'.join([YYYY, MM, DD])
    
    terms_info = {term[0]: int(term[2:]) for term in terms}
    expired_privacies = [i for i, privacy in enumerate(privacies, start=1) if today > get_expired_date(privacy[:-2], terms_info[privacy[-1]])]
                         
    return expired_privacies