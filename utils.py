from enum import StrEnum

class CourseType(StrEnum):
    """
    Enum for course types.
    """
    pc = "Professional Certificate"
    spl = "Specialization"
    sa = "Standalone"

class CertificateValue(StrEnum):
    """
    Enum for certificate values.
    """
    o = "Low"
    t = "Special Knowledge"
    f = "Moderate"
    s = "High"
