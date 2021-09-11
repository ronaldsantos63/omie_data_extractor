class OmieServiceException(Exception):
    pass


class OmieServiceBadRequestException(OmieServiceException):
    pass


class OmieServiceNotFoundException(OmieServiceException):
    pass
