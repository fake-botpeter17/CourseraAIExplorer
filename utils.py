from enum import StrEnum, IntEnum

class CourseType(StrEnum):
    """
    Enum for course types.
    """
    pc = "Professional Certificate"
    spl = "Specialization"
    sa = "Standalone"

class CertificateValue(IntEnum):
    """
    Enum for certificate values.
    """
    o = "Low"
    t = "Special Knowledge"
    f = "Moderate"
    s = "High"
