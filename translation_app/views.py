from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TranslationRequestSerializer, TranslationResponseSerializer
from .langchain_app import LangChainApp  # Import your LangChainApp class

class TranslateTextView(APIView):
    def post(self, request):
        serializer = TranslationRequestSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data['text']
            
            # Instantiate LangChainApp before calling translate_text
            langchain_app = LangChainApp()  
            
            translated_text = langchain_app.translate_text(input_text)  # Call your translation model here
            response_serializer = TranslationResponseSerializer({'translated_text': translated_text})
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        
        # If the input is not valid, return a 400 Bad Request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'translation_app/index.html')
