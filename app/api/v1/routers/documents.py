# from fastapi import APIRouter, UploadFile, File, Depends
# from app.services.ocr_service import OCRService, AuthService
# from app.schemas.document import (
#     DocumentStatus, ExtractedEvents, ConfirmSelection
# )

# router = APIRouter(prefix="/documents", tags=["OCR"])
# ocr_service = OCRService()
# auth_service = AuthService()

# @router.post("", status_code=201)
# async def upload_doc(file: UploadFile = File(...), current_user=Depends(auth_service.get_current_user)):
#     return await ocr_service.enqueue_document(current_user.id, file)

# @router.get("/{doc_id}/status", response_model=DocumentStatus)
# async def document_status(doc_id: int, current_user=Depends(auth_service.get_current_user)):
#     return await ocr_service.get_status(current_user.id, doc_id)

# @router.get("/{doc_id}/extracted", response_model=ExtractedEvents)
# async def document_extracted(doc_id: int, current_user=Depends(auth_service.get_current_user)):
#     return await ocr_service.get_extracted(current_user.id, doc_id)

# @router.post("/{doc_id}/confirm", status_code=200)
# async def document_confirm(
#     doc_id: int,
#     payload: ConfirmSelection,
#     current_user=Depends(auth_service.get_current_user)
# ):
#     return await ocr_service.confirm_selection(current_user.id, doc_id, payload)
